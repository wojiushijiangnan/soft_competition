from random import choice

import numpy as np
# 一个随机游走的类
class RandomWalk:
    # 默认点数五千
    def __init__(self, num_points=5000):
        self.num_points = num_points
        # 两个存储x和y轴坐标值的列表
        # 每次游走都从 0 0开始
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        # 不断游走 知道列表达到指定的的长度
        while len(self.x_values) < self.num_points:
            # 决定前进的方向和沿这个方向前进的距离 左右的
            x_direction = choice([-1, 1])
            # randon.choice(sequence)类型可以是list tuple str等
            # 返回序列中的个随机元素 传入空序列会返回异常
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            # 要么往左负的 往右正的 上下的
            y_direction = choice([-1, 1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            # 给元素定义 后存入列表
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)