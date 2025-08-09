import requests
# 图形化展示了github中最受欢迎的java项目
import matplotlib.pyplot as plt
import numpy as np
import json
url = "https://api.github.com/search/repositories"
url += "?q=language:java+sort:stars+stars:>10000"
headers = {"Accept": "application/vnd.github.v3+json"}

# 禁用代理
# 这里的r打印出来是一个键值对，要转化成jsion格式才可以
r = requests.get(url, headers=headers, proxies={"http": None, "https": None})
# 如果是两百就代表响应成功了
print(f'ok?:{r}')
#
# r = r.json()
# total_count = r["total_count"]
# print(f'total_count:{total_count}')
# result = r["incomplete_results"]
# print(f'result:{not result}')