from flask import Flask, request, jsonify
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from lxml import etree
import time

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
        image_info = []
        retries = 0
        max_retries = 20
        scroll_pause_time = 2
        while len(image_info) < self.num_images and retries < max_retries:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(scroll_pause_time)
            page_source = self.driver.page_source
            tree = etree.HTML(page_source)
            items = tree.xpath('//li[contains(@class,"imgitem")]/@data-objurl')
            image_info.extend(items[:self.num_images - len(image_info)])
            retries += 1
        return image_info

    def run(self, query):
        self.search_images(query)
        image_infos = self.parse_image_info()
        self.driver.quit()
        return image_infos

@app.route('/crawl_images', methods=['POST'])
def crawl_images():
    data = request.json
    query = data.get('query')
    num_images = data.get('num_images')
    if not query or not num_images:
        return jsonify({'error': 'Please provide both query and num_images'}), 400

    base_url = "https://images.baidu.com/"
    spider = BaiduImageSpider(base_url, num_images)
    image_urls = spider.run(query)

    results = [{'Image_name': f"image_{i+1}", 'Image_url': url} for i, url in enumerate(image_urls)]
    return jsonify(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
