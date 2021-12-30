import requests
from time import sleep
s = requests.Session()
for i in range(1,7200):
    sleep(1)
    s.get("http://localhost:9080/crawl.json?spider_name=gimmiproxy&url=https://gimmeproxy.com/api/getProxy")
