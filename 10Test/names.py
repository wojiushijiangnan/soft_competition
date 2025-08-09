from name_function import get_formatted_name

print('q exit')
while True:
    first = input('first name:')
    if first == 'q':
        break
    last = input('last name:')
    if last == 'q':
        break
    formatted_name = get_formatted_name(first, last)
    print(formatted_name)

    # 在测试这个方法的时候要运行一下 还要输入姓名 这太麻烦了 所以我们使用自动测试pytest
