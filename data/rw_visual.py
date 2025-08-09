import  matplotlib
from matplotlib import pyplot as plt

from randon_walk import RandomWalk

# 实例化类
rw = RandomWalk()
# 调用方法
rw.fill_walk()

# 指定画图模板
plt.style.use('classic')
# 调用subplots 返回画图对象
# fig表示画布 ax表示子图（绘图区域）
fig, ax = plt.subplots()
# 用子图绘制一个散点图
ax.scatter(rw.x_values,rw.y_values,s=15)
# 指定xy轴长度相等
ax.set_aspect('equal')
plt.show()

