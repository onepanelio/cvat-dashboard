import requests
from json2html import *
import json
import sys
import subprocess


def dump(task, name):
    output = subprocess.run('printenv | grep PATH_PREFIX', shell=True, stdout=subprocess.PIPE,
                            universal_newlines=True)

    wrksp = output.stdout[12:-2]
    url = "https://c.onepanel.io/" + wrksp + "/api/v1/tasks/" + str(task) + "/annotations/" + name
    with open('config.json','r') as json_file:
        headers = json.load(json_file)
    payload = ""

    response = requests.request("GET", url, data=payload, headers=headers)
    print(response)


if __name__ == "__main__":
    var = sys.argv[1].split(',')
    dump(var[0], var[1])
