# encoding: utf-8

import tushare as ts
import pandas as pd

# 获取股票列表
stock_list = ts.get_stock_basics()

# 循环获取股票历史行情
stock_his_info = []

for code in stock_list.index.tolist():
    stock_his_info.append(ts.get_k_data(code, start='2017-01-01', end='2017-07-31'))

df = pd.concat(stock_his_info)
df.to_csv('~/git-src/scratch/stock_his_info.csv')
