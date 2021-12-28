#!/usr/bin/env python
# coding: utf-8

import csv
import pandas as pd
import numpy as np
#get_ipython().run_line_magic('matplotlib', 'inline')
import glob


mylist = [f for f in glob.glob(".\\*.csv")]
print(mylist)

dfsonglist_all = pd.DataFrame()

for nextfile in mylist:
    dfFile = pd.read_csv(nextfile)
    dfsonglist_all =  pd.concat([dfsonglist_all, dfFile.drop(dfFile.columns[0], axis=1)], ignore_index=True)

dfsonglist_all.to_csv('all_list.csv')
print(dfsonglist_all.head())

dfsonglist = dfsonglist_all.drop_duplicates(subset=['date','time','artist','title'],keep='first')
dfsonglist.to_csv('full_list.csv')
print(dfsonglist.head())

dfsonglist.to_csv('full_list.csv')
