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
# 添加鼠标提示
repo_dicts = response_dict["items"]
repo_names, repo_links, stars, hover_texts = [], [], [], []
for repo_dict in repo_dicts:
    repo_names.append(repo_dict["name"])
    stars.append(repo_dict["stargazers_count"])

#     使用x轴作为标签
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_dict['name']}</a>"
    repo_links.append(repo_link)

# 创建悬停文本
# 提取每个项目的所有者和描述
    owner = repo_dict["owner"]["login"]
    description = repo_dict["description"]
    # plotly可以使用HTML代码
    hover_text = [f"{owner}<br />{description}"]
    hover_texts.append(hover_text)
#     hover_name参数把悬停给到可视化

title = "Most-Starred Python Projects on GitHub"
labels = {"x": "Repository", "y": "Stars"}


fig = px.bar(x = repo_links, y = stars,title=title, labels=labels,hover_name=hover_texts)
fig.update_layout(title_font_size=24,xaxis_title_font_size=18,yaxis_title_font_size=16)
# 。修改条形颜色 opacity透明度
fig.update_traces(marker_color='SteelBlue',marker_opacity=0.6)

fig.show()