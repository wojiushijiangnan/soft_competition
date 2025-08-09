from pandas.tseries import frequencies
import plotly.express as px

from die import Die

die = Die()

results = []
result = 0

for roll_num in range(1000):
    # 返回一个1~6的随机数
    result1 = die.roll()
    result2 = die.roll()
    result = result1 + result2
    results.append(result)

frequencies = []

poss_results = range(2,12)
print(poss_results)

for value in poss_results:
    # count方法会返回value在该列表中出现的次数
    frequency = results.count(value)
    frequencies.append(frequency)
print(frequencies)

# 对结果进行可视化
title = "666"
lables = {'x':'dianshu', 'y':'zhi'}
# bar表示柱形图 传入：x轴 y轴的值
fig = px.scatter(title=title, labels=lables, x=poss_results, y=frequencies)
fig.show()
