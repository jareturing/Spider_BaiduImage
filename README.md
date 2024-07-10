# 一、安装依赖
1. pip install -r requirements.txt
2. 安装谷歌浏览器
# 二、Image_Spider.py
> 该程序爬取图片到本地，并生成对应的csv文件
## 1.展示
> 爬取内容均来自于百度图片
例如输入：水利
生成压缩包：水利_Baidu.zip

内容展示：
- 文件夹：`Image\`
包含爬取的所有图片
  - 1.jpg
  - 2.jpg
  - ...
  - n.jpg
- CSV文件：`Image_info.csv`
包含`Image_name`, `Image_Title`图片来源的`Image_URL`
  - `Image_name`：对应`Image\` 文件夹中个图片的名称
  - `Image_Title` ：图片对应的标题
  - `Image_URL` ：该图片的来源来凝结

---
1. 压缩包中的文件
![image](https://github.com/xxhanzo/Spider_BaiduImage/assets/97886040/d3582e1e-6f2b-41a9-b1e1-74539560d20b)
2. 文件夹`Image\` 中的文件
![image](https://github.com/xxhanzo/Spider_BaiduImage/assets/97886040/d7a3c584-4f30-4468-96a0-e33407b0ed98)
3. `Image_info`中的文件
![image](https://github.com/xxhanzo/Spider_BaiduImage/assets/97886040/86b145e8-3d38-4d9e-b9e6-390569f0b8ec)
## 2.使用
1. 打开cmd面板，输入命令：
~~~ curl -X POST http://127.0.0.1:5000/crawl_images -H "Content-Type: application/json" -d "{\"query\": \"水利\", \"num_images\": 100}" ~~~
- 其中`"{\"query\": \"水利\", \"num_images\": 100}"`，`query`输入想要爬取的内容，例如：“水利”，“花”。。等。`num_images` 输入想要爬取的图片的数量，必须为正整数。
- 注意`\` 符号不可缺少
2. 下载压缩包，输入命令：
~~~ curl -O http://127.0.0.1:5000/download/水利_Baidu.zip ~~~
- 说明：其中`水利_Baidu.zip` 为你刚刚想要搜索的内容，例如你刚刚搜索内容为“花”，则此时输入命令为：
`curl -O http://127.0.0.1:5000/download/花_Baidu.zip`
## 3.使用流程图
![whiteboard_exported_image](https://github.com/xxhanzo/Spider_BaiduImage/assets/97886040/c60b5904-55d7-4a14-a4a8-214fc64bd571)

# 三、Image_Spider_JSON.py
> 该程序爬取搜索图片的url，通过url可以访问该图片
## 1.使用及展示
1. 打开cmd面板，输入命令：
curl -X POST http://127.0.0.1:5000/crawl_images -H "Content-Type: application/json" -d "{\"query\": \"水利\", \"num_images\": 5}"
- 其中`"{\"query\": \"水利\", \"num_images\": 100}"`，`query`输入想要爬取的内容，例如：“水利”，“花”。。等。`num_images` 输入想要爬取的图片的数量，必须为正整数。
- 注意`\` 符号不可缺少
2. 返回：
[{"Image_name":"image_1","Image_url":"https://slt.ah.gov.cn/group5/M00/05/22/wKg8v2OWiTyAHhJvAEx-hBMUUs8255.jpg"}]
- 其中`Image_name`为图片id
- `Image_url` 为图片的url，通过此url可以直接访问该图片。
