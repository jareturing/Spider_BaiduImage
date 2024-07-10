# Spider_BaiduImage
# Spider_Image
# 1.展示

> 爬取内容均来自于百度图片

例如输入：水利

生成压缩包：水利_Baidu.zip

内容展示：

- 文件夹：``Image\``
  - 包含爬取的所有图片
  - 1.jpg
  - 2.jpg
  - ...
  - n.jpg
- CSV文件：``Image_info.csv``
  - 包含``Image_name``, ``Image_Title``图片来源的``Image_URL``
  - ``Image_name``：对应``Image\`` 文件夹中个图片的名称
  - ``Image_Title`` ：图片对应的标题
  - ``Image_URL`` ：该图片的来源来凝结

1. 压缩包中的文件

![img](https://s1rdjxlut25.feishu.cn/space/api/box/stream/download/asynccode/?code=ZTkwODRhZDU3MmRiNDYzNDlkNmFkMTYwYjE5MGJjMjBfN3NXWm5PeUlGTGdTNE53eWUyZmhxaFBYbVZnRUpTTktfVG9rZW46VmdzOWI5Yk5ib0R5NHh4OEdjcGNrbDRMbk5tXzE3MjA1NzU2NTc6MTcyMDU3OTI1N19WNA)

1. 文件夹``Image\`` 中的文件

![img](https://s1rdjxlut25.feishu.cn/space/api/box/stream/download/asynccode/?code=ODllNjkwYzE4ZGJjZWI2NjE3OWRlNWM0MGI5OTUwMmFfZ3hlNWd5RkwxZXM1QXprVUlYMlJRM2pRSnFFaXcycDVfVG9rZW46TXY2dWI3bGNDb2s4RnF4aGRyZmNXNHFQbkhmXzE3MjA1NzU2NTc6MTcyMDU3OTI1N19WNA)

1. ``Image_info``中的文件

![img](https://s1rdjxlut25.feishu.cn/space/api/box/stream/download/asynccode/?code=MDAzMGY4MjNhMTE1YzE0YTNkYmFkMTdjM2M1OTU2MmRfdnZVSzBGT2h4MGhqSGM1dWNJM3p0M0N3TXJ1T082NGtfVG9rZW46R0Z1cmI0Q2czb1RBa3Z4YnBBT2NBMldkbkZmXzE3MjA1NzU2NTc6MTcyMDU3OTI1N19WNA)

# 2.使用

## 2.1 安装依赖

1. 依赖

暂时无法在飞书文档外展示此内容

1. 需安装谷歌浏览器

## 2.2 使用

1. 打开cmd面板，输入命令：

```Python
curl -X POST http://127.0.0.1:5000/crawl_images -H "Content-Type: application/json" -d "{\"query\": \"水利\", \"num_images\": 100}"
```

- 其中``"{\"query\": \"水利\", \"num_images\": 100}"``，``query``输入想要爬取的内容，例如：“水利”，“花”。。等。``num_images`` 输入想要爬取的图片的数量，必须为正整数。
- 注意``\`` 符号不可缺少

1. 下载压缩包，输入命令：

```Python
curl -O http://127.0.0.1:5000/download/水利_Baidu.zip
```

- 说明：其中``水利_Baidu.zip`` 为你刚刚想要搜索的内容，例如你刚刚搜索内容为“花”，则此时输入命令为：

```
curl -O ``http://127.0.0.1:5000/download/``花_Baidu.zip
```

# 3.使用流程图

![whiteboard_exported_image](https://github.com/xxhanzo/Spider_Image/assets/97886040/b077a65b-4c98-4860-bfef-cefd5229a3df)

