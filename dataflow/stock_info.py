# encoding: utf-8

import pandas as pd
import tushare as ts
import os


class StockInfoLoader(object):

    def __init__(self, store_path):
        self.store_path = store_path
        self.pro = ts.pro_api('baf51ad222163a131a10f5a8f51dd84a020ea713bebf2c3d4ad447fb')

    def download_stock_basic(self):
        df = self.pro.stock_basic()
        df.to_msgpack(self.store_path + 'stock_basic.msg')

    def load_stock_basic(self):
        if os.path.isfile(self.store_path + 'stock_basic.msg'):
            return pd.read_msgpack(self.store_path + 'stock_basic.msg')



if __name__ == '__main__':

    loader = StockInfoLoader('/Users/chenchen/jianguoyun/qvest_data/')
    loader.download_stock_basic()
    stock_basic = loader.load_stock_basic()