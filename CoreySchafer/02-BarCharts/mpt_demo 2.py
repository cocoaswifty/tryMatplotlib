import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from collections import Counter

plt.style.use('fivethirtyeight')    # 變更plt style # 沒有網格效果

data = pd.read_csv('CoreySchafer/02-BarCharts/data.csv')
ids = data['Responder_id']
lang_responses = data['LanguagesWorkedWith']

language_counter = Counter()

for response in lang_responses:
    language_counter.update(response.split(';'))

# print(language_counter)

languages = []
popularity = []

# print(list(map((lambda languages, popularity: zip(*language_counter.most_common(15)))))
# for item in language_counter.most_common(15):   # 取前面最多的15個
#     languages.append(item[0])
#     popularity.append(item[1])

# dict 取前面最多的15個 unzip to list
languages, popularity = map(lambda x: list(x), zip(*language_counter.most_common(15)))  

languages.reverse()
popularity.reverse()

plt.barh(languages, popularity)

plt.title('Most Popular Languages')
# plt.ylabel('Programming Languages')
plt.xlabel('Number of People Who Use')

plt.tight_layout()  # 圖表過度集中可以使用.tight_layout分開
plt.show()