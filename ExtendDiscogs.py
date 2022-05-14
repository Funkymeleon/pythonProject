import discogs_client
import pandas as pd
import numpy as np

# noinspection SpellCheckingInspection
d = discogs_client.Client('HR3superscraper/1.0', user_token='gBtrxcMPRJXQLzXiAkeDaLlLFusTmKWgAkcUSjRV')
#
# results = d.search('sia david guetta', type="Release")
# results.page(1)
#
# print(results[0].releases[2].genres)
# print(results[0].releases[2].year)

dfsonglist = pd.read_csv('./new_list.csv')

for index, row in dfsonglist.iterrows():
    results = d.search(row['artist'] + ' ' + row['title'], type="Release")
    try:
        page1 = results.page(1)

        if len(page1) > 0:
            print(row['artist'] + ' ' + row['title'] + ' ' + page1[0].data["genre"][0] + ' ' + page1[0].data["year"])
            dfsonglist.at[index, 'genre'] = page1[0].data["genre"][0]
            dfsonglist.at[index, 'year'] = int(page1[0].data["year"])
        else:
            print("No result: " + row['artist'] + ' ' + row['title'])
            dfsonglist.at[index, 'genre'] = np.nan
            dfsonglist.at[index, 'year'] = np.nan
        if index % 100 == 0:
            dfsonglist.to_csv('new_list.csv', index=False)
    except:
        dfsonglist.at[index, 'genre'] = np.nan
        dfsonglist.at[index, 'year'] = np.nan
