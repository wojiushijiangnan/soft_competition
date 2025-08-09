from random import  randint

class Die:
    # 方法定义的时候给了默认值6
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        # 返回一个1~6之间的随机值
        return randint(1, self.sides)