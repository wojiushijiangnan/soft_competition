from operator import itemgetter

# 导入requests包
import requests

# 指定一个url
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
# 用requests.get（url）方法得到响应对象
r = requests.get(url, proxies={"http": None, "https": None})
print(f"Status code: {r.status_code}")

# 把响应对象转化为json
submission_ids = r.json()
# 创建一个新的列表 一会用来存储
submission_dicts = []

# 循环5个id
for submission_id in submission_ids[:5]:
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url, proxies={"http": None, "https": None})
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    # 存储单独一个id的相关信息
    response_dict = r.json()
    # 创建了一个字典
    submission_dict = {
        'title': response_dict['title'],
        'link': f"http://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict['descendants'],
    }
    # 将字典添加到列表
    submission_dicts.append(submission_dict)
    # 给列表排序 第一个参数是你要给谁排序？（这必须是一个可迭代对象）
    # key=len按元素长度排序 key=str.lower忽略大小写排序 key=itemgetter('key")按照对应的值排序
    # revers=True按照降序排序
    submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                             reverse=True)

    # 打印这个列表中的字典
    for submission_dict in submission_dicts:
        print(f"\nTitle: {submission_dict['title']}")
        print(f"Discussion link: {submission_dict['link']}")
        print(f"Comments: {submission_dict['comments']}")