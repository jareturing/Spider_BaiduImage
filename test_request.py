import requests
import json


def process_request(url,keyword='水利',num_images=100):
    headers={'Content-Type':'application/json'}
    post_data={
        "query": keyword,
        "num_images":num_images
    }
    respose=requests.post(url,data=json.dumps(post_data),headers=headers)
    print(respose)
    if respose.status_code!=401:
        data=respose.json()
    return data




if __name__=='__main__':
    url='http://127.0.0.1:5000/crawl_images'
    # url = 'http://127.0.0.1:8000/crawl_images'
    keyword='狗'
    num_image=1000
    keywords = ["绝缘手套", "绝缘靴", "靴子", "手套","工装"]
    for keyword in keywords:
        res=process_request(url=url,keyword=keyword,num_images=num_image)
        print(res)


# curl -X POST http://127.0.0.1:5000/crawl_images -H "Content-Type: application/json" -d "{\"query\": \"水利\", \"num_images\": 100}"
# curl -X POST http://127.0.0.1:8000/crawl_images -H "Content-Type: application/json" -d "{\"query\": \"狗\", \"num_images\": 10}"

