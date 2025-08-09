import json
from pathlib import Path

path = Path('users.json')
def writ_users():
    name = input('name:')
    age = input('age:')
    city = input('city:')

    users = {}
    users['name'] = name
    users['age'] = age
    users['city'] = city
    j_users = json.dumps(users)
    path.write_text(j_users, encoding='utf-8')

def red_user():
    lines = path.read_text(encoding='utf-8')
    # 读到以后再进行反序列化
    lines = json.loads(lines)
    return lines

#接收用户的多个属性并持久化完成读写