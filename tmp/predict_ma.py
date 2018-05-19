# encoding: utf-8

import numpy as np
import tushare as ts
import pandas as pd


myts = ts.get_hist_data('sh', start='2017-01-01', end='2017-05-07')
