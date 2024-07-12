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
curl -X POST http://127.0.0.1:5000/crawl_images -H "Content-Type: application/json" -d "{\"query\": \"水利\", \"num_images\": 100}" 
- 其中`"{\"query\": \"水利\", \"num_images\": 100}"`，`query`输入想要爬取的内容，例如：“水利”，“花”。。等。`num_images` 输入想要爬取的图片的数量，必须为正整数。
- 注意`\` 符号不可缺少
2. 下载压缩包，输入命令：
curl -O http://127.0.0.1:5000/download/水利_Baidu.zip
- 说明：其中`水利_Baidu.zip` 为你刚刚想要搜索的内容，例如你刚刚搜索内容为“花”，则此时输入命令为：
`curl -O http://127.0.0.1:5000/download/花_Baidu.zip`
## 3.使用流程图
![whiteboard_exported_image](https://github.com/xxhanzo/Spider_BaiduImage/assets/97886040/c60b5904-55d7-4a14-a4a8-214fc64bd571)

# 三、Image_Spider_JSON.py
> 该程序爬取搜索图片的url，通过url可以访问该图片
> 该程序在Ubuntu系统上部署的步骤
## 1.安装必要的软件
确保系统已更新，且安装了python3和pip，如已安装请忽略此步骤。
sudo apt update
sudo apt upgrade
sudo apt install python3 python3-pip
## 2.设置虚拟环境
sudo apt install python3-venv
python3 -m venv myenv
source myenv/bin/activate
## 3.安装Flask和依赖
pip install Flask selenium lxml webdriver-manager
## 4.安装Chrome和ChromeDriver
### 4.1安装Chrome
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
sudo apt-get install -f
### 4.2安装ChromeDriver
1. 首先查看下载的Chrome版本是什么版本，执行：`google-chrome --version`
![image](https://github.com/user-attachments/assets/f38cc9f0-0dc2-4e09-95c9-f2ab84e399af)
例如我的这里是：126.0.6478.126
2. 这里是下载地址：
  1. 114之前版本的下载地址：http://chromedriver.storage.googleapis.com/index.html
  2. 126以后版本的下载地址：https://googlechromelabs.github.io/chrome-for-testing/#canary
  3. 复制下载链接：（我的版本链接为）：https://storage.googleapis.com/chrome-for-testing-public/126.0.6478.126/linux64/chromedriver-linux64.zip
![image](https://github.com/user-attachments/assets/f4628cb8-1331-404e-9a65-d725cb6d157d)
  4. 执行命令下载ChromeDriver（为你刚刚复制的链接）
wget https://storage.googleapis.com/chrome-for-testing-public/126.0.6478.126/linux64/chromedriver-linux64.zip
  5. 安装：
unzip chromedriver_linux64.zip
sudo mv chromedriver /usr/local/bin/
sudo chmod +x /usr/local/bin/chromedriver
### 5.运行
1. 激活虚拟环境（为自己创建的虚拟环境）
source myenv/bin/activate
2. cd到`Image_Spider` 文件夹下，执行
python Image_Spider_JSON.py
### 6.使用
运行成功后应该能看到以下信息：
![image](https://github.com/user-attachments/assets/35fed359-603d-4467-81f3-d21254744c8e)
1. 在本地执行命令：
curl -X POST http://172.18.231.238:8000/crawl_images -H "Content-Type: application/json" -d "{\"query\": \"狗\", \"num_images\": 10}"
2. 其中：
  1. 端口号设置为：8000
  2. ` http://172.18.231.238:8000`改为本机地址
  3. `"{\"query\": \"狗\", \"num_images\": 10}"`中的`query`为要搜索的内容，`10` 为要搜索的数量。
3. 运行结果：
![image](https://github.com/user-attachments/assets/fe06e979-550a-4e24-bcdf-86a479c203a5)
## 7.可能出现的问题
### 7.1 如果运行不了可能是驱动地址不对
1. 查看驱动地址，执行命令：`which chromedriver`
root@iZuf6297pykaabwpfitucnZ:~# which chromedriver
/usr/local/bin/chromedriver
2. 将代码中的`chromedriver_path ` 修改为你的地址：
[图片]
### 7.2  有的图片网址可能加载不出来，是百度图片的问题，大部分网址都是有图片的。

