#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import cufflinks as cf
import seaborn as sns


# In[2]:


dfsonglist = pd.read_csv('full_list.csv', usecols=['date','time','artist','title'])
dfsonglist['artist'] = dfsonglist['artist'].str.lower().str.strip().str.replace(' ','')
dfsonglist['title'] = dfsonglist['title'].str.lower().str.strip().str.replace(' ','')
dfsonglist


# In[3]:


#Anzahl wie häufig ein Künstler gespielt wurde
artist_count = dfsonglist.groupby(by=['artist'], as_index=False).size().sort_values('size')#.to_frame('count')
artist_count


# ## Top 10 der Artists played

# In[4]:


#Die meist gespielten Songs
top_played_songs = dfsonglist.groupby(by=['artist','title']).size().to_frame('count')
top_played_songs.sort_values('count')[-10:]


# In[5]:


#Songs eines Künstlers die gespielt wurden
#Die Summe müsste die Anzahl des Künstlers total sein
#songs_from_artist = artist_count.index.tolist()[-10:]
songs_from_artist = artist_count["artist"].tolist()[-10:]
print(songs_from_artist[-3])
top_played_songs.loc[songs_from_artist[-3]]

#Kurve zeigt ab wann ein Song durchstartet.
top_played_songs.sort_values('count').plot(figsize=[10,5])

#Histogramm über die Anzahl gespielter Songs
#top_played_songs.iplot(kind='hist', x='count')

#Anzahl der Songs pro Artist played in a week

# ## Anzahl der Lieder pro Tag

#Erzeuge einen neuen Index für alle 'date'
idx = pd.date_range(dfsonglist['date'].min(), dfsonglist['date'].max())

#gruppiere die Songs pro 'date'
songs_per_day_count = dfsonglist.groupby(by=['date']).size().to_frame('count').sort_values('date')

#Unklar was ein DatetimeIndex genau ist. Irgendwie wird der Index des Dataframe dadurch geändert
#Womöglich konvertiert es den Index von einem string zu einem Datum (Format DatetimeIndex)
songs_per_day_count.index = pd.DatetimeIndex(songs_per_day_count.index)

#Reindizieren. Dabei wird ein neuer DF erstelllt, welche jedem IDX Index einen Wert zuweist. Entweder aus dem songs_per_day oder 0
songs_per_day = songs_per_day_count.reindex(idx, fill_value=0)
#songs_per_day.iplot()


# ## Wochenzusammenfassung wann welcher Song aufkam und wann er runter ging

top_five_played_songs = top_played_songs.sort_values('count')[-5:]

art = top_five_played_songs.index.get_level_values('artist')
son = top_five_played_songs.index.get_level_values('title')

it = range(len(art))

for x in it:
    dfArtSongWeek = dfsonglist[ (dfsonglist['artist'] == art[x]) & (dfsonglist['title'] == son[x])]
    dfArtSongWeek['week'] = pd.to_datetime(dfArtSongWeek['date']).dt.isocalendar().week
    dfWeekArtTitle = dfArtSongWeek.groupby(by=['week','artist','title']).size().to_frame('count')
    dfWeekArtTitle['count'].plot(use_index=False)
    print(dfWeekArtTitle.index.get_level_values('title')[0])

#Counter können auch verwendet werden um die Anzahl von Elemente in einer Liste zusammen zu fassen.
from collections import Counter
EasyCountTitle = Counter(dfsonglist.loc[:,'title'])


# Anzahl der Duplikate Songs pro Tag
# 
# Verhältnis zum Anzahl der Songs
# 
# Top Songs im letzten Monat
# 
# Meistgespielter Song des Jahres
#