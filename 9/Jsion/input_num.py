#问用户喜欢什么数字，存储起来
# 有就打印 没有就问
import json
from pathlib import Path


def ask_num():
    num = input('num:')
    # d 是变成json djDJ
    num = json.dumps(num)
    path.write_text(num, encoding='utf-8')


def red_num():
    num = path.read_text(encoding='utf-8')
    # load是返回字符串 lowlow的字符串
    num = json.loads(num)
    return num

path = Path('test.json')
if path.is_file():
    print(red_num())
else:
    ask_num()