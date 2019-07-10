import requests
from json2html import *
import json
def dump(task):
    url = "https://c.onepanel.io/onepanel-demo/projects/cvat-public-demo/workspaces/cvat-gpu-4/label/tensorflow/annotation/create/task/1"
    payload = ""
    headers = {
        'Authorization': "Basic YWRtaW46cGFzc3dvcmQ=",
        'cache-control': "no-cache",
        'Postman-Token': "23423423423423",
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'

        }

    response = requests.request("GET", url, data=payload, headers=headers)
if __name__ == "__main__":
    idx=sys.var[1]
    dump(idx)