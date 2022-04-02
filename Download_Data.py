import os
import requests
import os.path
from os import path

def download_file(url, filename):
    print('Downloading File')
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as file:
            for chunk in response:
                file.write(chunk)
            
def downloadData():
    csvDataDict = {"US_youtube_trending_data.csv": "1KRDhh-5xgZq8llBMd4MEJ6HbySpetZb5" , 
                   "GB_youtube_trending_data.csv" : "1fRKOWSIhz7g9NUbgPgdeORfrye_BoQ-w" , 
                   "CA_youtube_trending_data.csv" : "1G5CCfV_-NcuyuZgLy-0sVy9O_qUAiJz1",
                   "US_category_id.json" : "1v7BeZCp__eKU_gu-CyBpTsYF4rWStPub",
                   "GB_category_id.json" : "1raD8wcVoo4yR8M6HoGuH_FURhjstu8MY",
                   "CA_category_id.json" : "1686kv7DWe1TNBBsmrfmy9eUMv0mSK0r6",}
    
    if path.isdir("data/") == False:
        os.mkdir("data/")
    for fileName, fileId in csvDataDict.items():
        url = 'https://drive.google.com/u/2/uc?id='+fileId+'&export=download&confirm=t'
        location = 'data/'+ fileName
        download_file(url, location)         

    print('Files Download completed')