import numpy as np
from matplotlib import pyplot as plt

from study.data.randon_walk import RandomWalk

# 实例化对象 生成两个有五千个随机整数的列表
rw = RandomWalk()
# 调用生成随机数的方法
rw.fill_walk()

# 这里传入的是默认值五千 从0到五千返回等间隔为1的值
point_numbers = np.arange(rw.num_points)

points = np.array([rw.x_values, rw.y_values])
# 得到绘图对象
ax ,fig = plt.subplots(figsize=(10, 10), dpi=1080)



