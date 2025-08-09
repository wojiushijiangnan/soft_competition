from pathlib import Path

from mpmath import mp
import time

# 设置精度为十万位小数
mp.dps = 100000  # dps = decimal places

print("开始计算 π 的值（10万位）...")
start_time = time.time()

# 获取 π 的高精度值（转换为字符串）
pi_str = str(mp.pi())

# 写入文件
filename = "pi_digits.txt"
with open(filename, "w", encoding="utf-8") as f:
    f.write(pi_str)

end_time = time.time()
print(f"写入完成，文件保存为：{filename}")
print(f"耗时：{end_time - start_time:.2f} 秒\n")

# 用户输入生日并验证
user_birthday = input("请输入你的生日（仅限月日，例如 0101 表示1月1日）：").strip()

while True:
    if not user_birthday:
        user_birthday = input("输入不能为空，请重新输入你的生日（例如 0405）：").strip()
    elif not user_birthday.isdigit() or len(user_birthday) != 4:
        user_birthday = input("格式错误，请输入4位数字（例如 0405）：").strip()
    else:
        print("\n开始匹配...")
        break

# 查找生日是否出现在 π 的小数中
if user_birthday in pi_str:
    index = pi_str.index(user_birthday)

    # 输出匹配位置
    print(f"🎉 匹配成功！你的生日出现在 π 的第 {index} 位（从 0 开始计数）")

    # 输出前后各 10 位
    start_idx = max(0, index - 10)
    end_idx = index + len(user_birthday) + 10
    context = pi_str[start_idx:end_idx]

    print(f"上下文显示（前后各10位）：\n{context}")
else:
    print("❌ 匹配失败，你的生日未出现在前10万位 π 中。")


# 先读取所有行一起打印 再读取所有行分开打印
path = Path("pi_digits.txt")
context = path.read_text(encoding="utf-8")
context_lines = context.splitlines()
print("\n所有行一起打印：")
print(context)

print("\n所有行分开打印：")
for line in context_lines:
    print(line)