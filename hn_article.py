import requests
# 要求：获得https://hacker-news.firebaseio.com/v0/item/31353677.json响应并打印
url = 'https://hacker-news.firebaseio.com/v0/item/31353677.json'
response = requests.get(url,proxies={"http": None, "https": None})
print(f'直接打印response（url的响应）：{response.json()}')
# 把json转成字符串
import json
# 4个空格作为缩进单位
print(f'转换后的数据：{json.dumps(response.json(), indent=4)}')