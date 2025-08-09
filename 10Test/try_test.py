"""
写一个员工类
包含姓名、年龄、工资属性
一个give_raise方法
将默认月薪设为50000
同时也接受其他的月薪

编写一个测试文件，测试默认和修改方法是否正常。
写一个夹具来测试
"""

# 定义一个员工类
class Employee:
    # 编写初始化方法 传入名字 年龄 和初始化工资
    def __init__(self, name, age, salary=5000):
        self.name = name
        self.age = age
        self.salary = salary

    #编写获得工资的方法，工资应该默认为五千，如果不给我穿参数就是默认5000
    def give_raise(self,salary=None):
        # 不给参数
        if salary is None or salary <= 0:
            self.salary = 5000
            # ⚠️这里返回self 而不是salary
            return self.salary
        # 给参数 else
        else:
            # ⚠️ 这里不要把等式写反了
            self.salary = salary
            return salary
