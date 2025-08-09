from pathlib import Path

path = Path('alice.txt')
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")
else:
    # split 按照单词切割
    words = contents.split()
    num_words = len(words)
    print(f"The file {path} has about {num_words} words.")

# 静默失败
# 在except中添加pass即可


# 两数相加，当有数字不是int时告诉用户
# ❌
# flag = True
# while flag:
#     a = int(input('num:'))
#     b = int(input('num:'))
#     if a == 'q':
#         flag = False
#         break
#     if b == 'q':
#         flag = False
#         break
#     elif a != int:
#         print(f'{a} is not an integer.')
#         continue
#     elif b != int:
#         print(f'{b} is not an integer.')
#         continue
# print(a + b)

# 两数相加，当有数字不是int时告诉用户
# ❌得用sum 后面在转为int
# flag = True
# while flag:
#     a = int(input('num:'))
#     b = int(input('num:'))
#     if a == 'q':
#         break
#     elif not isinstance(a,int):
#         print('num must be an integer')
#         continue
#     elif not isinstance(b,int):
#         print('num must be an integer')
#         continue
# print(a+b)

# ❌不能用elif来判断异常 应该用except
# flag = True
# while flag:
#     a = input('num:')
#     b = input('num:')
#     if a == 'q':
#         break
#     elif not isinstance(a,int):
#         print('num must be an integer')
#         continue
#     elif not isinstance(b,int):
#         print('num must be an integer')
#         continue
# print(a+b)

flag = True
while flag:
    a = input('num:')
    b = input('num:')
    if a == 'q':
        break
    if b == 'q':
        break
    try:
        a = int(a)
        b = int(b)
        print(a+b)
    except ValueError:
        print('value Error')
        continue #在用户犯错后可以继续输入