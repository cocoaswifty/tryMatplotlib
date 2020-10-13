# https://myapollo.com.tw/zh-tw/python-itertools-more-itertools/
from itertools import count
import random
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []

index = count() # 從0開始計算，每次加1

def animate(i):
    # x_vals.append(next(index))
    # y_vals.append(random.randint(0, 5))

    # plt.cla()   # 清除當前圖形中活動坐標的軸 axis，換句話說，其他軸將保持不變。
    # plt.plot(x_vals, y_vals)

    data = pd.read_csv('CoreySchafer/09-LiveData/data.csv')
    x = data['x_value']
    y1 = data['total_1']
    y2 = data['total_2']

    plt.cla()   # 清除已存在的線條
    plt.plot(x, y1, label='Channel 1')
    plt.plot(x, y2, label='Channel 2')

    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.savefig('CoreySchafer/09-LiveData/plot.png')


ani = FuncAnimation(plt.gcf(), animate, interval=1000) # 1秒鐘運行一次 animate()


plt.tight_layout()

plt.show()
