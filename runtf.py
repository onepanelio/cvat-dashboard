import requests
from json2html import *
import json
import subprocess
import sys


def dump(task, wrksp):
    with open('config.json','r') as json_file:
        headers = json.load(json_file)
    url = "https://c.onepanel.io/" + wrksp + "tensorflow/annotation/create/task/1 "
    payload = ""
    response = requests.request("GET", url, data=payload, headers=headers)


if __name__ == "__main__":
    output = subprocess.run('printenv | grep PATH_PREFIX', shell=True, stdout=subprocess.PIPE,
                            universal_newlines=True)
    wrksp = output.stdout[12:]
    idx = sys.var[1]
    dump(idx, wrksp)
