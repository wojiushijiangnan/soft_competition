# 一个操作文件的库（模块=python代码）
# Path pathlib 的一个类
from pathlib import Path

# path指向一个文件
path = Path('pi_digits.txt')
# read_txt读取文件内容的一个方法
# 会把读到的所有文本都解析成字符串
# 这个方法读到文件的末尾会返回一个空字符串
# 空字符串被打印出来就是一个空行 也就是说读到末尾会进行自动换行
contents = path.read_text()
print(f'contents: {contents}  break.')
# 删除右边的空白字符串
contents = contents.rstrip()
# 方法链式调用
contents = path.read_text().strip()
print(contents)

print('\n')

# 如何读取行？
path = Path('pi_digits.txt')
contents = path.read_text()
# 按行切割好 放到一个列表中
# ['1'
#  '2']
lines = contents.splitlines()
for line in lines:
    print(line)
print('\n')

# 按照行来读取 然后打印所有字符串一共有多少位
path = Path('pi_digits.txt')
contents = path.read_text()
# lines的长度是三行
# lines也是一个list 里面放的是把每行文本变成列表里的一个元素
lines = contents.splitlines()
print(f'lines:{lines}')
total_string = ''
# 实现字符串拼接最好给需要拼接的字符串赋值
for line in lines:
    # ❌ 这样做是不可以的 因为line在超出for后就会被丢弃 必须保存在total_string中
    total_string += line
    print(f'单独的line:{line}')

print(len(total_string))

print(f'lines:{type(lines)}')

# 计算一行里有几个重复的字符串
line = 'row,row,row,5546,Row'
word = 'row'
count = line.lower().count(word)
print(count)
