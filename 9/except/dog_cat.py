#存入两条毛和两条狗第二行
# 读取这些文件 并添加健壮性
from pathlib import Path

path = Path('dog.txt')
for i in range(2):
    cat = input('cat name')
    dog = input('dog name')
    path.write_text(f'{cat} {dog}\n')
    # ⚠️会重新写入 而不是追加 改为列表会更好 或者字典

try:
    context = path.read_text(encoding='utf-8')
    print(context)
except FileNotFoundError:
    print('file not found')

# 静默失败添加pass

