import json
from pathlib import Path

path = Path('test.json')
# lines = [1,2,3]
# # json.dumps方法接受一个要转换成Json的数据，然后会返回一个字符串
# content = json.dumps(lines)
# path.write_text(content)

# read.txt 只可以读取txt文本 但是json是特殊的txt格式
print(json.loads(path.read_text(encoding='utf-8'))
)

# 接受用户的信息 写入到json文件
# name = input('name:')
# name = json.dumps(name)
# path.write_text(name)

# 读取用户名 并打印 实现了用户名的持久化 哪怕程序退出 数据依然不会丢失
lines = path.read_text(encoding='utf-8')
content = json.loads(lines)
print(content)