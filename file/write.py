from pathlib import Path
from sys import flags

# 如果指向的文件不存在会自动创建
# 如果指定的文件已存在，write_text()将删除其内容，
# 并将指定的内容写入其中
path = Path('write_test.txt')
# write_text方法只接受一个实参，就是你要写入的字符串
# 只可以String类型，不可以写入其他类型
# 如果要写入其他类型必须先用str（ ）函数进行转换
# 必须在字符串中写入\n 文本才会实现换行
string = ('Hello World\n'
          'python\n'
          'python\n')
path.write_text(string)

# 接受用户的名字 然后存入文件
path = Path('name.txt')
name = input('请输入你的名字：')
path.write_text(name, encoding='utf-8')

# 接收用户名 每个用户名独占一行
flags = True
while flags:
    path = Path('names.txt')
    names = input('请输入多个名字：')
    path.write_text(names + '\n', encoding='utf-8')
    if names == '':
        flags = False
