# https://mofanpy.com/tutorials/data-manipulation/plt/
# https://blog.techbridge.cc/2018/05/11/python-data-science-and-machine-learning-matplotlib-tutorial/
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation

# x = np.linspace(-3, 3, 50)
# y1 = 2*x+1
# y2 = x**2

# plt.figure(figsize=(5,3))
# plt.plot(x,y1)

# plt.figure(figsize=(5,3))
# plt.plot(x,y2, label='up')
# plt.plot(x,y1, color='red', linewidth=2.0, linestyle='--', label='down')
# plt.legend()    # 使用label添加圖例


# plt.xlim((-1,2))    # 取值範圍
# plt.xlim((-2,3))
# plt.xlabel('x')
# plt.ylabel('y')

# new_ticks = np.linspace(-1,2,5) # 更換ticks
# print(new_ticks)
# plt.xticks(new_ticks)
# plt.yticks([-2, -1, 0, 1, 2], ['0', '25', '50', '75', '100'])

# ax = plt.gca()  # 調整坐標軸
# ax.spines['right'].set_color('none')
# ax.spines['top'].set_color('none')
# ax.xaxis.set_ticks_position('bottom')
# ax.yaxis.set_ticks_position('left')
# ax.spines['bottom'].set_position(('data',-1))
# ax.spines['left'].set_position(('data',0))


# #--註解
# x0 = 1
# y0 = 2*x0 + 1
# plt.scatter(x0, y0, s=50, color='b')
# plt.plot([x0,x0], [y0,0], 'k--', lw=2.5)
# plt.annotate(r'$2x+1=%s$' % y0, xy=(x0,y0), xycoords='data', xytext=(+30, -30), textcoords='offset points', fontsize=16, arrowprops=dict(arrowstyle='->', connectionstyle='arc3, rad=.2'))
# plt.text(0.2, 7, 'This is the some text.')


# plt.show()

 
## ----柱狀圖

# n = 12
# x = np.arange(n)
# y1 = (1 - x/float(n)) * np.random.uniform(0.5, 1.0, n)

# plt.figure(figsize=(5,3))
# plt.bar(x, y1, facecolor='#9999ff', edgecolor='#ff9999')

# for x, y in zip(x, y1):
#     plt.text(x, y + 0.02, f'{y:.2f}', ha='center', va='bottom')

# plt.show()


## ----多合一顯示

# plt.figure()

# plt.subplot(2,2,1)
# plt.plot([0,1],[0,1])

# plt.subplot(2,2,2)
# plt.plot([0,1],[0,2])

# plt.subplot(2,2,3)
# plt.plot([0,1],[0,3])

# plt.subplot(2,2,4)
# plt.plot([0,1],[0,4])
# plt.show()

# --多合一顯示，方法二
# fig, ((ax11), (ax12)) = plt.subplots(1,2, sharex=True, sharey=True, figsize=(3,5))
# ax11.scatter([1,2],[1,2])
# ax11.set_aspect(2)
# ax12.set_aspect(1)


# plt.tight_layout()
# plt.show()


# ----圖中圖

# fig = plt.figure()
# x = [1,2,3,4,5,6,7]
# y = [1,3,4,2,5,8,6]

# left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
# ax1 = fig.add_axes([left, bottom, width, height])
# ax1.plot(x,y,'r')

# left, bottom, width, height = 0.2, 0.5, 0.3, 0.3
# ax2 = fig.add_axes([left, bottom, width, height])
# ax2.plot(x,y,'r')
# ax2.set_title('inside 1')

# plt.axes([0.6, 0.2, 0.3, 0.3])
# plt.plot(y[::-1],x,'g')
# plt.title('inside 2')

# plt.show()


# ----Animation


# fig, ax = plt.subplots()

# x = np.arange(0, 2*np.pi, 0.01)
# line, = ax.plot(x , np.sin(x))

# def animate(i):
#     line.set_ydata(np.sin(x+i/100))
#     return line,

# def init():
#     line.set_ydata(np.sin(x))
#     return line,

# ani = animation.FuncAnimation(fig=fig,func=animate,frames=100, init_func=init, interval=10, blit=False)
# plt.show()


# ---- real time 

# plt.axis([0, 10, 0, 1])

# for i in range(10):
#     y = np.random.random()
#     plt.scatter(i, y)
#     plt.pause(0.05)

# plt.show()