import json
from pathlib import Path

"""
如果文件存在就读取并打印用户名
文件不存在就问用户叫什么 然后写入文件
"""
path = Path('test.json')
def get_user():
    lines = path.read_text(encoding='utf-8')
    j_lines = json.loads(lines)
    return j_lines

def writ_user():
    name = input('name:')
    lines = json.dumps(name)
    path.write_text(lines, encoding='utf-8')
    return name

if path.exists():
    print(get_user())
else:
    print(writ_user())

