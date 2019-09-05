# encoding: utf-8

import pandas as pd
import tushare as ts
import os
import datetime


class TradingInfoLoader(object):

    def __init__(self, store_path):
        self.store_path = store_path
        self.pro = ts.pro_api('baf51ad222163a131a10f5a8f51dd84a020ea713bebf2c3d4ad447fb')

    def load_trading_info_single(self, ts_code, update=False):
        if os.path.isfile(self.store_path + '/' + ts_code + '.msg') and not update:
            return pd.read_msgpack(self.store_path + '/' + ts_code + '.msg')
        else:
            current_day = datetime.date.today().strftime("%Y%m%d")
            daily = self.pro.daily(ts_code=ts_code, start_date='20170101', end_date=current_day)
            daily.to_msgpack(self.store_path + '/' + ts_code + '.msg')
            return daily


if __name__ == '__main__':
    loader = TradingInfoLoader('/Users/chenchen/jianguoyun/qvest_data/')
    test = loader.load_trading_info_single('002419.SZ', update=True)


