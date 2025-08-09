import matplotlib.pyplot as plt

from study.data.scatter import y_values

# 绘制前五个正整数的立方，再绘制前五千个
x_values = range(1,6)
y_values = [ i**3 for i in x_values]

plt.style.use('fivethirtyeight')
fig, ax = plt.subplots()
ax.set_title('Square Numbers',fontsize=20)
ax.set_xlabel('Value',fontsize=20)
ax.set_ylabel('Value',fontsize=20)
ax.tick_params(axis='both', which='major', labelsize=20)

# 绘制散点图
ax.scatter(x_values, y_values, s=10, c=y_values, cmap=plt.cm.Blues, edgecolors='k')
plt.show()