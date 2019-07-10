import requests
from json2html import *
import json
def dump(task,name):
    import subprocess
    import pandas as pd
    import sys
    output = subprocess.run('printenv | grep PATH_PREFIX', shell=True, stdout=subprocess.PIPE, 
                            universal_newlines=True)

    wrksp=output.stdout[12:]
    url = "https://c.onepanel.io/"+wrksp+"api/v1/tasks/"+str(task)+"/annotations/"+name

    payload = ""
    headers = {
        'Authorization': "Basic YWRtaW46cGFzc3dvcmQ=",
        'cache-control': "no-cache",
        'Postman-Token': "23423423423423",
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'

        }

    response = requests.request("GET", url, data=payload, headers=headers)
if __name__ == "__main__":
#     print(sys.argv)
    var=sys.argv[1].split(',')
#     print(var)
    dump(var[0],var[1])
#     process('onepanel-demo/datasets/cat-dog','tets')
