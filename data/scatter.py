import matplotlib.pyplot as plt
# 优先定义数值
x_values = [1,2,3,4,5,6,7,8]
y_values = [1,2,3,4,5,6,7,8]

# 通过循环来生成值
x_values = range(1,1001)
y_values = [x**2 for x in x_values]
plt.style.use('fivethirtyeight')
fig, ax = plt.subplots()
# s表示点的像素大小200
# c关联颜色映射
# cmap告诉pyplot使用哪个颜色进行映射
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues,  s=10)
ax.set_title('Square Numbers',fontsize=20)
ax.set_xlabel('Age',fontsize=20)
ax.set_ylabel('Salary',fontsize=20)
# 设置刻度 which的意思是
ax.tick_params(axis='both', which='major', labelsize=20)
ax.ticklabel_format(style='plain')
# 设置坐标轴的取值范围
ax.axis([0,1100, 0, 1_100_000])
# 将plt.show()转换为plt.savefig('squares_plot.png',bbox_inches='tight')
# plt.show()
# 第二个参数表示把第二个夺取的空白区域删除
# 使用path可以把输出文件放在任何地方
plt.savefig('scatter.png',bbox_inches='tight')
