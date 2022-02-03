#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import glob
import re


mylist = [f for f in glob.glob(".\\csv\\*.csv")]
print(mylist)

dfsonglist_all = pd.DataFrame()

for nextfile in mylist:
    dfFile = pd.read_csv(nextfile)
    dfsonglist_all = pd.concat([dfsonglist_all, dfFile.drop(dfFile.columns[0], axis=1)], ignore_index=True)

dfsonglist_all.to_csv('all_list.csv')
print(dfsonglist_all.head())
print()

dfsonglist = dfsonglist_all.drop_duplicates(subset=['date', 'time', 'artist', 'title'], keep='first')


#dfsonglist = pd.read_csv('../../pythonProject/full_list.csv', usecols=['date','time','artist','title'])
dfsonglist['artist_stripped'] = [(re.sub('\W+','', string).lower()) for string in dfsonglist['artist']]
dfsonglist['title_stripped'] = [(re.sub('\W+','', string).lower()) for string in dfsonglist['title']]
dfsonglist = dfsonglist.sort_values(by = ['date','time'], ignore_index = True)
#dfsonglist

#Add year to dataframe
dfsonglist['year']=pd.to_datetime(dfsonglist['date']).dt.year

#Add weekday to dataframe
dfsonglist['weekday']=[x.weekday() for x in pd.to_datetime(dfsonglist['date'])]
#dfsonglist


dfsonglist.to_csv('full_list.csv', index=False)

print(dfsonglist.head())
print(dfsonglist.shape)