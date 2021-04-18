# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import requests
import csv
from bs4 import BeautifulSoup
import time
from datetime import date
from datetime import timedelta
import random
import pandas as pd
import numpy as np


if __name__ == '__main__':

    titles = list()
    artists = list()
    times = list()
    dates = list()

    for days_before in range(0, 15):
        check_date = date.today() + timedelta(days=-days_before)
        formatted_date = check_date.strftime('%Y-%m-%d')

        urls = [f"https://www.hr3.de/playlist/playlist_hrthree-100~_date-{formatted_date}_hour-{i}.html" for i in range(0,24)]

        for url in urls:
            titles_tmp = list()
            artists_tmp = list()
            time_tmp = list()
            response = requests.get(url)

            html = BeautifulSoup(response.text, 'html.parser')

            titles_html = html.find_all('span', class_="c-epgBroadcast__headline text__headline")
            artist_html = html.find_all('span', class_="c-epgBroadcast__subline text__subline")
            time_html = html.find_all('div', class_="c-epgBroadcast__time")

            for title in titles_html:
                titles_tmp.append(title.text.strip('\n'))

            titles_tmp.reverse()
            titles.append(titles_tmp)

            for artist in artist_html:
                artists_tmp.append(artist.text.strip('\n'))

            artists_tmp.reverse()
            artists.append(artists_tmp)

            for time_l in time_html:
                time_tmp.append(time_l.text.strip('\n'))

            time_tmp.reverse()
            times.append(time_tmp)

            dates.append([formatted_date] * len(times))

            time.sleep(0.2 + random.random())
            print(f'{url} finished')

        print(f'{formatted_date} finished')

    artists = [item for sublist in artists for item in sublist]
    titles = [item for sublist in titles for item in sublist]
    times = [item for sublist in times for item in sublist]

    dates = [item for sublist in dates for item in sublist]

    df_data = pd.DataFrame(zip(dates, times, artists, titles), columns = ['date', 'time', 'artist', 'title'])
    print(df_data.head())

    df_data.to_csv(r'./titles.csv')

    #with open('./titles.csv', 'w', newline='') as myfile:
     ##   wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
       # wr.writerow(zip(titles, artists))