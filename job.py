import requests
from json2html import *
import json
import subprocess
with open('config.json') as json_file:
    headers = json.load(json_file)

output = subprocess.run('printenv | grep PATH_PREFIX', shell=True, stdout=subprocess.PIPE,
                        universal_newlines=True)
wrksp = output.stdout[12:]

url = "https://c.onepanel.io/" + wrksp + "api/v1/tasks/1"

# url = "https://c.onepanel.io/onepanel-demo/projects/cvat-public-demo/workspaces/cvat-gpu-4/label/tensorflow
# /annotation/create/task/1"
payload = ""

response = requests.get( url, headers=headers)