import requests
import plotly.express as px


url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"
headers = {"Accept": "application/vnd.github.v3+json"}

# 禁用代理
# 这里的r打印出来是一个键值对，要转化成jsion格式才可以
r = requests.get(url, headers=headers, proxies={"http": None, "https": None})
print(f'ok?:{r}')

# 处理结果
response_dict = r.json()
print(f"Complete results: {not response_dict['incomplete_results']}")

# 处理仓库的相关信息
repo_dicts = response_dict["items"]
repo_names, stars = [], []
for repo_dict in repo_dicts:
    repo_names.append(repo_dict["name"])
    stars.append(repo_dict["stargazers_count"])

# 可视化
title = "Most-Starred Python Projects on GitHub"
labels = {"x": "Repository", "y": "Stars"}
fig = px.bar(x = repo_names, y = stars,title=title, labels=labels)
fig.update_layout(title_font_size=24,xaxis_title_font_size=18,yaxis_title_font_size=16)
fig.show()