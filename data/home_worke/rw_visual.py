from matplotlib import pyplot as plt

from random_walk import RandomWalk
from study.data.mpl_squares import x_values

rw = RandomWalk()
fig, ax = plt.subplots()
rw.fill_walk()
num = list(range(5000))
ax.plot(rw.x_values, rw.y_values,linewidth=5,s=1,c=num,cmap=plt.cm.Blues)
print(rw.x_values, rw.y_values,num)

plt.show()