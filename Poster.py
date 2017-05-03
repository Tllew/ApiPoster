import requests
from Settings import url
from Settings import uniqueKey
from Settings import urlHeads
from jsonCreator import createJson
from multiprocessing.dummy import Pool as ThreadPool
import time

def post(data):

    resultList = []
    result = {}

    pool = ThreadPool(5)
    count = 0;
    data = [x for x in data]
    for x in data:
        jsonVal = createJson(dict(x))

        if uniqueKey:
            result.update(jsonVal)
            if count == 5000 or count == len(data) - 1:
                resultList.append(result)
                count = 0;
                result = {}
        else:
            resultList.append(jsonVal)
        count +=1

    pool.map(postToUrl, resultList)


def postToUrl(data):
    sent = False
    tries = 0
    while not sent:
        try:
            tries += 1
            r = requests.post(url,headers=urlHeads, json=data)
            sent = r.status_code in [200,202]
        except Exception as e:
            print("Failue due to :%s"%e)
            time.sleep(1)
            sent = tries > 3