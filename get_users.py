import requests
from json2html import *
import json
import subprocess
import pandas as pd
import sys

with open('config.json','r') as json_file:
    headers = json.load(json_file)

output = subprocess.run('printenv | grep PATH_PREFIX', shell=True, stdout=subprocess.PIPE,
                        universal_newlines=True)

wrksp = output.stdout[12:-2]
url = "https://c.onepanel.io/" + wrksp + "/api/v1/users/1"
payload = ""

response = requests.request("GET", url, data=payload, headers=headers)
data_processed = json.loads(response.text)

d = data_processed
data = {'email': d['email'], 'last_login': d['last_login']}

formatted_table = json2html.convert(json=data)
print(formatted_table)
