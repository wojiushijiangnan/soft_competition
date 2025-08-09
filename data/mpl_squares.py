import matplotlib.pyplot as plt

# 定义一个列表
squares = [1,4,9,16,25,36,49,64]

# 默认第一个数据会对应x的0坐标
x_values = [1,2,3,4,5,6,7,8]
# 采取默认的样式
plt.style.use('fivethirtyeight')
# fig表示整个图像
# ax表示图像中的绘图
fig, ax = plt.subplots()
# plot开始绘图`
# 参数的逗号后面➕空格
# 第一个参数是x坐标轴的值，第二个是y轴，第三个是线的宽度
# y轴和x轴的取数数量要对应
ax.plot(x_values, squares, linewidth=2)
# 标题
ax.set_title('Square Numbers',fontsize=20)
# 横轴标签
ax.set_xlabel('Value',fontsize=20)
ax.set_ylabel('Square of Value',fontsize=20)
# 设置刻度的样式
ax.tick_params(labelsize=20)
plt.show()
