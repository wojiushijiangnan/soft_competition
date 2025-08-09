try:
    print(5/0)
except ZeroDivisionError:
    print('Caught ZeroDivisionError')

while True:
    a = input("num:")
    b = input("den:")
    if a or b == 'q':
        break
    a = int(a)
    b = int(b)
    try:
        print(a/b)
    except ZeroDivisionError:
        print('Caught ZeroDivisionError')
        continue
