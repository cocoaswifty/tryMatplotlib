# 5筆資料以下才用圓餅圖，超過5筆資料建議用直方圖呈現
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')    # 變更plt style # 沒有網格效果

# slices = [60, 40, 30, 20]
# labels = ['Sixty', 'Forty', 'Extra1', 'Extra2']
# colors = ['#008fd5', '#fc4f30', '#e5ae37', '#6d904f']

# Language Popularity
slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
explode = [0, 0, 0, 0.1, 0] # 炸開，分格區塊

plt.pie(slices, labels=labels, explode=explode, shadow=True, startangle=90, 
        autopct='%1.1f%%', wedgeprops={'edgecolor': 'black'})

plt.title('Pie Chart')
plt.tight_layout()  # 圖表過度集中可以使用.tight_layout分開
plt.show()