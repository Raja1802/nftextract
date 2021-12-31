import pymongo
import urllib
import requests
client = pymongo.MongoClient("mongodb://ajar:" + urllib.parse.quote_plus("Raja@1802") + "@cluster0-shard-00-00.1vax0.mongodb.net:27017,cluster0-shard-00-01.1vax0.mongodb.net:27017,cluster0-shard-00-02.1vax0.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-umkr09-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.nft
collect = db["gimmiproxy"]
li = []
# for i in range(1,10):
#     prox = list(collect.aggregate([{'$sample': {'size': 1 }}]))
#     li.append(prox[0]["proxy"]["curl"])
#     print(prox[0]["proxy"]["curl"])

s = requests.Session()
response = s.get(url="https://gimmeproxy.com/api/getProxy")
data = response.json()
print(data["curl"])