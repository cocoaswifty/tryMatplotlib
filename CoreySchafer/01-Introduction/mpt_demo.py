# 格式化字符串
# https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html

from matplotlib import pyplot as plt

# print(plt.style.available)    #顯示所有style
# plt.style.use('fivethirtyeight')    # 變更plt style # 沒有網格效果
plt.xkcd()  # xkcd 漫畫風格 # 沒有網格效果

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

# Median Python Developer Salaries by Age
py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

plt.plot(ages_x, py_dev_y, color='#5a7d9a', linewidth=3, label='Python')

# Median JavaScript Developer Salaries by Age
js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]

plt.plot(ages_x, js_dev_y, color='#adad3b', linewidth=3, label='JavaScript')

# Median Developer Salaries by Age
dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]

plt.plot(ages_x, dev_y, color='#444444', linestyle='--', marker='.', label='All Devs')

plt.xlabel('Ages')
plt.ylabel('Median Salary')
plt.title('Median Salary by Age')

# plt.legend(['All Devs', 'Python'])
plt.legend()    # 顯示標籤
plt.grid()  # 添加網格
plt.tight_layout()  # 圖表過度集中可以使用.tight_layout分開
plt.savefig('CoreySchafer/01-Introduction/plot.png')
plt.show()