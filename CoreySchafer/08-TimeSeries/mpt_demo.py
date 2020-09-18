import pandas as pd
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates

plt.style.use('seaborn')

# dates = [
#     datetime(2019, 5, 24),
#     datetime(2019, 5, 25),
#     datetime(2019, 5, 26),
#     datetime(2019, 5, 27),
#     datetime(2019, 5, 28),
#     datetime(2019, 5, 29),
#     datetime(2019, 5, 30)
# ]

# y = [0, 1, 3, 4, 6, 5, 7]

# plt.plot_date(dates, y, linestyle='solid')

# plt.gcf().autofmt_xdate()   # 讓日期傾斜

# # https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
# date_format = mpl_dates.DateFormatter('%b, %d %Y')  # 轉換日期格式

# plt.gca().xaxis.set_major_formatter(date_format)


data = pd.read_csv('CoreySchafer/08-TimeSeries/data.csv')
data['Date'] = pd.to_datetime(data['Date']) # 轉換成 datetime
data.sort_values('Date', inplace=True)  # 排序

price_date = data['Date']
price_close = data['Close']

plt.plot_date(price_date, price_close, linestyle='solid')

plt.gcf().autofmt_xdate()   # 讓日期傾斜

plt.title('Bitcoin Prices')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.tight_layout()
plt.savefig('CoreySchafer/08-TimeSeries/plot.png')
plt.show()