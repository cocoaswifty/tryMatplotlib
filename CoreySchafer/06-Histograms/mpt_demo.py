import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

data = pd.read_csv('CoreySchafer/06-Histograms/data.csv')
ids = data['Responder_id']
ages = data['Age']

bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

plt.hist(ages, bins=bins, edgecolor='black', log=True)  # 取log 不然80以上資料太少不會顯示

median_age = 29
color = '#fc4f30'

plt.axvline(median_age, color=color, linewidth=2, label='Age Median')    # 顯示中位數線條

plt.legend()

plt.title('Ages of Respondents')
plt.xlabel('Ages')
plt.ylabel('Total Respondents')

plt.tight_layout()

plt.show()