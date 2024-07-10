from flask import Flask, request, jsonify, send_file
import os
import time
import requests
import csv
from concurrent.futures import ThreadPoolExecutor, as_completed
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from lxml import etree, html
import zipfile

app = Flask(__name__)


class BaiduImageSpider:
    def __init__(self, base_url, num_images):
        self.base_url = base_url
        self.num_images = num_images
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # 设置无头模式
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920x1080")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    def search_images(self, query):
        self.driver.get(self.base_url)
        search_box = self.driver.find_element(By.NAME, "word")
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)

    def parse_image_info(self):
        time.sleep(5)  # 等待页面加载
        image_info = []  # 存储图片信息
        retries = 0
        max_retries = 20  # 增加重试次数
        scroll_pause_time = 2
        while len(image_info) < self.num_images and retries < max_retries:
            page_source = self.driver.page_source
            tree = etree.HTML(page_source)
            items = tree.xpath('//li[@class="imgitem"]')
            for item in items:
                image_url = item.xpath('.//img[@class="main_img img-hover"]/@src')
                image_title = item.xpath('./@data-title')
                image_data_url = item.xpath('./@data-fromjumpurl')
                if image_url and image_title and image_data_url:
                    clean_title = html.fromstring(image_title[0]).text_content()  # 清除HTML标签
                    image_info.append({
                        'image_url': image_url[0],
                        'image_title': clean_title,
                        'image_data_url': image_data_url[0]
                    })
                if len(image_info) >= self.num_images:
                    break
            # 模拟滚动页面加载更多图片
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(scroll_pause_time)  # 等待新图片加载
            retries += 1
        return image_info

    def download_image(self, image_info, folder, index):
        try:
            response = requests.get(image_info['image_url'], timeout=5)
            if response.status_code == 200:
                image_name = f"{index + 1}.jpg"
                image_path = os.path.join(folder, image_name)
                with open(image_path, 'wb') as file:
                    file.write(response.content)
                return {
                    'Image_name': image_name,
                    'Image_Title': image_info['image_title'],
                    'Image_URL': image_info['image_data_url']
                }
        except Exception as e:
            pass
        return None

    def download_images(self, image_infos, query):
        folder_name = f"{query}_Baidu"
        image_folder = os.path.join(folder_name, "Image")
        if not os.path.exists(image_folder):
            os.makedirs(image_folder)

        csv_file_path = os.path.join(folder_name, "Image_info.csv")
        image_data_list = []

        with ThreadPoolExecutor(max_workers=32) as executor:  # 增加线程数
            futures = [
                executor.submit(self.download_image, info, image_folder, index)
                for index, info in enumerate(image_infos)
            ]
            for future in as_completed(futures):
                result = future.result()
                if result:
                    image_data_list.append(result)

        image_data_list.sort(key=lambda x: int(x['Image_name'].split('.')[0]))

        with open(csv_file_path, 'w', newline='', encoding='utf-8-sig') as csvfile:  # 使用utf-8-sig编码
            fieldnames = ['Image_name', 'Image_Title', 'Image_URL']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for data in image_data_list:
                writer.writerow(data)

        return folder_name

    def run(self, query):
        self.search_images(query)
        image_infos = self.parse_image_info()
        actual_num_images = len(image_infos)
        folder_name = self.download_images(image_infos, query)
        self.driver.quit()
        return actual_num_images, folder_name


def create_zip(folder_name):
    zip_file_name = f"{folder_name}.zip"
    with zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_name):
            for file in files:
                zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), folder_name))
    return zip_file_name


@app.route('/crawl_images', methods=['POST'])
def crawl_images():
    data = request.json
    query = data.get('query')
    num_images = data.get('num_images')
    if not query or not num_images:
        return jsonify({'error': 'Please provide both query and num_images'}), 400

    base_url = "https://images.baidu.com/"
    spider = BaiduImageSpider(base_url, num_images)
    actual_num_images, folder_name = spider.run(query)

    zip_file_name = create_zip(folder_name)

    return jsonify({
        'actual_num_images': actual_num_images,
        'zip_file_name': zip_file_name
    })


@app.route('/download/<path:filename>', methods=['GET'])
def download_file(filename):
    directory = os.path.dirname(os.path.abspath(__file__))
    return send_file(os.path.join(directory, filename), as_attachment=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
