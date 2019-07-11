import requests
from json2html import *
import json
import subprocess
import pandas as pd
import sys
import json

with open('config.json') as json_file:
    headers = json.load(json_file)

output = subprocess.run('printenv | grep PATH_PREFIX', shell=True, stdout=subprocess.PIPE,
                        universal_newlines=True)
wrksp = output.stdout[12:]

url = "https://c.onepanel.io/" + wrksp + "api/v1/tasks"
# url = "https://c.onepanel.io/onepanel-demo/projects/cvat-public-demo/workspaces/cvat-gpu-4/label/api/v1/tasks"

payload = ""


response = requests.request("GET", url, data=payload, headers=headers)
data_processed = [json.loads(response.text)]
data = data_processed[0]['results']
next_p = data_processed[0]['next']
while next_p is not None:
    url = next_p
    response = requests.get(url, headers=headers)
    data_processed = [json.loads(response.text)]
    data += data_processed[0]['results']
    next_p = data_processed[0]['next']

tasks = []
for task in data:
    for i in ['url', 'size', 'mode', 'owner', 'assignee', 'bug_tracker', 'created_date', 'updated_date', 'overlap',
              'segment_size', 'z_order', 'flipped', 'segments']:
        del task[i]
    temp = []
    for i in task['labels']:
        del i['attributes']
        temp.append(i)
    task['labels'] = temp
    tasks.append(task)

data = json.dumps(tasks)
formatted_table = json2html.convert(json=data)

print(formatted_table)
