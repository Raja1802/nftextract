import requests
import os
import time 
s = requests.Session
def deletefiles():
    dirr = 'C:\\Users\\G RAJA\\Desktop\\ajarani.me\\ipfs\\'
    for f in os.listdir(dirr):
        os.remove(os.path.join(dirr, f))
headers = {'accept': 'application/json','Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkaWQ6ZXRocjoweDgzYTZhNDQ5ZTI0MjM4ZGEyNDg0NThFRDljQzA5NjA0NGQwMUNiNzgiLCJpc3MiOiJuZnQtc3RvcmFnZSIsImlhdCI6MTY0MTY0OTg0MzYyMiwibmFtZSI6InNmc2RmZHMifQ.5Ek8H4dN70JOKcZSIeqC81UjHilt2U58SpGustpNu30'}
for filename in os.listdir(r"C:\Users\G RAJA\Desktop\ajarani.me\ipfs"):  
    fff = open(f"C:\\Users\\G RAJA\\Desktop\\ajarani.me\\ipfs\\{filename}", 'rb')
    files = {'file': fff}
    r = requests.post(url="https://api.nft.storage/upload", files=files, headers=headers,stream=True)
    rsp = r.json()
    print(r.json())
    print(rsp["value"]["cid"], rsp["value"]["files"][0]["name"])
    cid=rsp["value"]["cid"]
    name=rsp["value"]["files"][0]["name"]
    print(f"https://{cid}.ipfs.dweb.link/{name}")
    time.sleep(10)
    fff.close()
    deletefiles()
