#如果文件存在 就把读取后转化为json
import json
from pathlib import Path

path = Path('test.json')
if path.exists():
    lines = path.read_text(encoding='utf-8')
    # 接收一个json 变成字符串 jsonLoad要加载json嘛
    content = json.loads(lines)
    print(content)
else:
    username = input('name:')
    # 接收字符串 变成json
    content = json.dumps(username)
    path.write_text(content)
# 如果文件不存在就写入这个json

