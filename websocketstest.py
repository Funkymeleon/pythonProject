#!/usr/bin/env python

import asyncio
import json
import pandas as pd
import csv
from websockets import connect
from datetime import datetime


async def getcurrentsong(uri):

    fieldn = ["title", "artist", "start"]
    async with connect(uri) as webs:
        # await webs.send("Hello world!")
        while 1:
            json_result = json.loads(await webs.recv())
            print(json_result)
            if "current" in json_result:
                CurrentSong = json_result["current"]
                CurTitle = CurrentSong["title"]
                CurArtist = CurrentSong["artist"]
                CurStart = CurrentSong["start"]
                # print(CurStart)
                # print(type(CurStart))
                dateStart = datetime.fromtimestamp(CurStart/1000.0)
                CurTime = dateStart.strftime('%Y-%m-%d %H:%M:%S')

                print(CurTime + " - " + CurArtist + " - " + CurTitle)
                del CurrentSong['id']
                del CurrentSong['artistImage']

                with open('test4.csv', 'a') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=fieldn)
                    writer.writeheader()
                    print(type(CurrentSong))
                    writer.writerows(CurrentSong)


                # argh = pd.DataFrame.from_dict(data=CurrentSong)

                # df_data = pd.DataFrame(argh)
                # df_data.to_csv('dict_file.csv', header=False, mode='a')

asyncio.run(getcurrentsong("wss://push.hr.de/push/web/HR3?version=v2"))
