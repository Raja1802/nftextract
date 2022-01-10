from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time
from time import sleep
import schedule 
import random
import pymongo
import urllib
import requests
s = requests.Session()

download_dir = "/app/download/"

# CHROMEDRIVER_PATH = r"C:\Users\G RAJA\Desktop\scrapy_mongo\scraper\chromedriver.exe"
GOOGLE_CHROME_PATH = "/app/.apt/usr/bin/google-chrome"
CHROMEDRIVER_PATH = "/app/.chromedriver/bin/chromedriver"
client = pymongo.MongoClient("mongodb://ajar:" + urllib.parse.quote_plus("Raja@1802") + "@cluster0-shard-00-00.1vax0.mongodb.net:27017,cluster0-shard-00-01.1vax0.mongodb.net:27017,cluster0-shard-00-02.1vax0.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-umkr09-shard-0&authSource=admin&retryWrites=true&w=majority")
mydb = client.anime
mycol = mydb["ggspider_dat"]
mongocol = mydb["gganime_videos_data"]
mydoc = mycol.find()
from pandas import json_normalize
df = json_normalize(mydoc)
df.shape
df.dropna(inplace=True)
df = df[0:1000]

def deletefiles():
    dirr = os.environ.get("download_dir")
    for f in os.listdir(dirr):
        os.remove(os.path.join(dirr, f))

def wait_for_downloads():
    while any([filename.endswith(".crdownload") for filename in os.listdir(os.environ.get("download_dir"))]):
        print("processing...")
        sleep(2)
# def uploadtoMongo():

def uploadtoipfs():
    headers = {'accept': 'application/json','Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkaWQ6ZXRocjoweDgzYTZhNDQ5ZTI0MjM4ZGEyNDg0NThFRDljQzA5NjA0NGQwMUNiNzgiLCJpc3MiOiJuZnQtc3RvcmFnZSIsImlhdCI6MTY0MTY0OTg0MzYyMiwibmFtZSI6InNmc2RmZHMifQ.5Ek8H4dN70JOKcZSIeqC81UjHilt2U58SpGustpNu30'}
    for filename in os.listdir(os.environ.get("download_dir")):  
        fff = open(f"{os.environ.get('download_dir')}+{filename}", 'rb')
        files = {'file': fff}
        r = requests.post(url="https://api.nft.storage/upload", files=files, headers=headers,stream=True)
        fff.close()
        return r.json()

def enable_download(driver):
    driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
    params = {
    'cmd': 'Page.setDownloadBehavior',
    'params': {
        'behavior': 'allow',
        'downloadPath': os.environ.get("download_dir")
    }
    }
    driver.execute("send_command", params)

def setting_chrome_options():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.binary_location = GOOGLE_CHROME_PATH
    chrome_options.add_argument('--no-sandbox')
    return chrome_options


for index, rowe in df.iterrows():
    browser = webdriver.Chrome(executable_path = os.environ.get("CHROMEDRIVER_PATH"), options = setting_chrome_options())
    enable_download(browser)
    # driver.get(DOWNLOAD_URL)
    url=rowe["download_1"]
    try:
        browser.get(url=url)
        time_1 = random.randint(5,7)
        sleep(time_1)
        sleep(10)
    except:
        print("failed to load page")
    # try:
    time_2 = random.randint(5,7)
    sleep(2)
    options = browser.find_elements_by_css_selector("div.dowload > a")
    options.click()
    sleep(time_2)
    sleep(30)
    wait_for_downloads()
    up_m = uploadtoipfs()

    # upload to mongoDB
    cid=up_m["value"]["cid"]
    name=up_m["value"]["files"][0]["name"]
    lin = f"https://{cid}.ipfs.dweb.link/{name}"
    mongo_li = {"link": lin,  "tracker": rowe["_id"], "ipfs_meta": dict(up_m), "episode_meta": dict(rowe)}
    dup_check = mongocol.find({'tracker':rowe["_id"]}).count()
    if dup_check == 0 :     
        mongocol.insert_one(dict(mongo_li))
        print ("video Added!")
    else:
        print("video Exist")
    print("insert completed")
    print("downloaded the video")
    # except:
    #     try:
    #         time_2 = random.randint(5,7)
    #         sleep(2)
    #         options = browser.find_element_by_css_selector("#content-download > div:nth-child(1) > div:nth-child(5) > a")
    #         options.click()
    #         sleep(time_2)
    #         sleep(30)
    #         wait_for_downloads()
    #         up_m = uploadtoipfs()
    #         # upload to mongoDB
    #         cid=up_m["value"]["cid"]
    #         name=up_m["value"]["files"][0]["name"]
    #         lin = f"https://{cid}.ipfs.dweb.link/{name}"
    #         mongo_li = {"link": lin, "tracker": rowe["_id"],"ipfs_meta": dict(up_m), "episode_meta": dict(rowe)}
    #         dup_check = mongocol.find({'tracker':rowe["_id"]}).count()
    #         if dup_check == 0 :     
    #             mongocol.insert_one(dict(mongo_li))
    #             print ("video Added!")
    #         else:
    #             print("video Exist")
    #         print("insert completed")
    #         print("downloaded the video")
    #     except:
    #         try:
    #             time_2 = random.randint(5,7)
    #             sleep(2)
    #             options = browser.find_elements_by_class_name("dowload")
    #             options.click()
    #             sleep(time_2)
    #             sleep(30)
    #             wait_for_downloads()
    #             up_m = uploadtoipfs()

    #             # upload to mongoDB
    #             cid=up_m["value"]["cid"]
    #             name=up_m["value"]["files"][0]["name"]
    #             lin = f"https://{cid}.ipfs.dweb.link/{name}"
    #             mongo_li = {"link": lin, "tracker": rowe["_id"],"ipfs_meta": dict(up_m), "episode_meta": dict(rowe)}
    #             dup_check = mongocol.find({'tracker':rowe["_id"]}).count()
    #             if dup_check == 0 :     
    #                 mongocol.insert_one(dict(mongo_li))
    #                 print ("video Added!")
    #             else:
    #                 print("video Exist")
    #             print("insert completed")
    #             print("downloaded the video")
    #         except:
    #             print("failed all stages")
    #     print("failed to download the video")
    deletefiles()
    browser.quit()