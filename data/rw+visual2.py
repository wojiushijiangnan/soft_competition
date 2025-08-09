from matplotlib import pyplot as plt

import randon_walk

"""突出每次游走的正要特征
    炳然分散注意力的元素不那么显眼
    为此，要先确定突出的元素
    比如：七点、重点和经过的路径
    再确定不需要那么显眼的元素，如可读标记和标签
    刻度标记：代表固定值的小短线
    标签：刻度代表的具体数值
    
    我们将使用颜色映射来指出游走中各个点的先后顺序，
    并删除每个点的黑色轮廓，让其颜色更加明显。
    为了根据游走中各个点的先后顺序进行着色，传递参数c，并将其设置为一个列表，
    其中包含各点的先后顺序。由于这些点是按顺序绘制的，
    因此给参数c指定的列表只需包含数0～4999"""

for i in range(5):
    #创建一个实例
    rw = randon_walk.RandomWalk()
    rw.fill_walk()

    #将所有点绘制出来
    plt.style.use('classic')
    # 调整输出尺寸，是一个元组
    fig, ax = plt.subplots(figsize=(10, 10), dpi=1080)

    # 这里传入的值是RandomWalk的构造方法的默认值五千 c是颜色 cmap是颜色映射 e是边缘颜色
    # range是按顺序生成整数 ⚠️不是随机生成 g 瞬狙 random才是随机生成
    point_numbers = range(rw.num_points)
    # scatter方法是绘制输入的单个点
    ax.plot(rw.x_values,rw.y_values,s=1, c=point_numbers,
           cmap=plt.cm.Blues,
               edgecolors='none', linewidths=0.5)
    ax.set_aspect('equal')

    # 突出起点和终点
    ax.plot(0,0, c='green', edgecolors='none', s=100)
    ax.plot(rw.x_values[-1],rw.y_values[-1], c='red', edgecolors='none', s=100)

    # 隐藏坐标轴 先获取每条坐标轴 再对坐标轴设置不可见
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()


