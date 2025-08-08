import requests

url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"
headers = {"Accept": "application/vnd.github.v3+json"}

# 禁用代理
# 这里的r打印出来是一个键值对，要转化成jsion格式才可以
r = requests.get(url, headers=headers, proxies={"http": None, "https": None})
print(f"r:{type(r)}")
print(f"Status code: {r.status_code}")

# 将响应转化为字典
response_dict = r.json()

print({response_dict['total_count']})
print(not response_dict['incomplete_results'])
repo_dicts = response_dict['items']
print(len(repo_dicts))
repo_dict = repo_dicts[0]
print(len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)


for repo_dict in repo_dicts:
    print(f"Name: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")


