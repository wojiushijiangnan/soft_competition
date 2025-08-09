from random import choice

# 定义一个类，为什么要定义一个类？
# 为了实现解耦吧？算了，不重要的
class RandomWalk:
    # 初始化方法
    def __init__(self,num_points=5000):
        self.num_points = num_points
        # 所有的随机游走都开始于0 让每次游走都从0,0出发
        self.x_values = [0]
        self.y_values = [0]

    # 选择方向
    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            # 会返回-1或者1
            x_direction = choice([-1,1])
            x_distance = choice([0,1,2,3,4,5,6,7,8])
            x_step = x_direction * x_distance

            y_direction = choice([-1,1])
            y_distance = choice([0,1,2,3,4,5,6,7,8])
            y_step = y_direction * y_distance

            # 在上一步的基础上去走下一步
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            if x_step == 0 and y_step == 0:
                continue

            # 把走了的这一步记录起来
            self.x_values.append(x)
            self.y_values.append(y)

# 绘制随机游走地图


