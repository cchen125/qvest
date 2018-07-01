# encoding: utf-8

import tushare as ts
import pickle

# 获取股票列表
stock_list = ts.get_stock_basics()

# 循环获取股票历史行情
stock_hist_data = {}
start_dt = '2015-01-01'
end_dt = '2018-06-30'

counter = 0
for code in stock_list.index.tolist():
    counter += 1
    print(counter)
    stock_hist_data[code] = ts.get_hist_data(code, start=start_dt, end=end_dt)

output = open('./stock_hist_data.pkl', 'wb')
pickle.dump(stock_hist_data, file=output)

# file_to_read = open('./stock_hist_data.pkl', 'rb')
# res = pickle.load(file_to_read)
