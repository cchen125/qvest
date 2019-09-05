# encoding: utf-8

import pandas as pd
import tushare as ts
import os
from dateutil.parser import parse
from config import token
import matplotlib.pyplot as plt


class Stock(object):

    def __init__(self, stock_code):
        self.stock_code = stock_code
        self.ts = ts
        self.ts.set_token(token)
        self.trading_info = None

    def get_trading_info(self, start_date, end_date):
        df = self.ts.pro_bar(ts_code=self.stock_code, adj='qfq', start_date=start_date, end_date=end_date)
        df['trade_date'] = df.trade_date.apply(lambda x: parse(x))
        df = df.set_index('trade_date').sort_index()
        self.trading_info = df

    def plot_trading_info(self):
        plt.plot(self.trading_info['close'])


if __name__ == '__main__':
    pass
