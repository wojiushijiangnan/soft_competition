#用pip安装pytest
# 单元测试：核实函数的某个方面没有问题
# 测试用例就是一组（多个）单元测试 核实函数的各个方面都没有问题
# 测试文件的名称很重要，要以test_打头，因为pytest会查找以test打头的文件和函数
# 如何启动pytest？只要在终端输入pytest就可以了
# 前提是你要先切换到正确的文件目录下
# 测试方法是要传入实参并且要进行断言的

from name_function import get_formatted_name
def test_first_lat_name():
    """能正确处理Janis JopLin这样的姓名吗？"""
    formatted_name = get_formatted_name('janis','joplin')
    # 告诉程序正确的值应该是什么样子的
    assert  formatted_name == 'Janis Joplin'

"""定义函数
测试函数
交互程序
要分开写在不同的py文件中"""