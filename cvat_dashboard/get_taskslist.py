import requests
from json2html import *
import json
def get_label(task):
    url ="https://c.onepanel.io/onepanel-demo/projects/cvat-public-demo/workspaces/cvat-gpu-4/label/api/v1/tasks/"+str(task)
    payload = ""
    headers = {
        'Authorization': "Basic YWRtaW46cGFzc3dvcmQ=",
        'cache-control': "no-cache",
        'Postman-Token': "23423423423423",
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'

        }

    response = requests.get( url, headers=headers)
    labels=response.json()
    labels['labels']
    label={}
    for i in labels['labels']:
        label[i['id']]=i['name']
    return label

def get_annot(task):
    url = "https://c.onepanel.io/onepanel-demo/projects/cvat-public-demo/workspaces/cvat-gpu-4/label/api/v1/tasks/"+str(task)+"/annotations"
    payload = ""
    headers = {
        'Authorization': "Basic YWRtaW46cGFzc3dvcmQ=",
        'cache-control': "no-cache",
        'Postman-Token': "23423423423423",
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'

        }

    response = requests.get( url, headers=headers)
    label=get_label(task)
    result = response.json()
    data={}
    for l_id in list(label.values()):
        data[l_id]=0
    data['total_objects']=len(result['shapes'])
    for annot in result['shapes']:
        l_id=annot['label_id']
        cl_name=label[l_id]
        if cl_name not in data.keys():
            data[cl_name]=1
        else:
            data[cl_name]+=1
    return data

import subprocess
import pandas as pd
import sys
output = subprocess.run('printenv | grep PATH_PREFIX', shell=True, stdout=subprocess.PIPE, 
                        universal_newlines=True)

wrksp=output.stdout[12:]
url = "https://c.onepanel.io/"+wrksp+"api/v1/tasks"
url = "https://c.onepanel.io/onepanel-demo/projects/cvat-public-demo/workspaces/cvat-gpu-4/label/api/v1/tasks"

# annotated=get_annot(1)
# print(url)
payload = ""
headers = {
    'Authorization': "Basic YWRtaW46cGFzc3dvcmQ=",
    'cache-control': "no-cache",
    'Postman-Token': "23423423423423"
    }

response = requests.request("GET", url, data=payload, headers=headers)
data_processed = [json.loads(response.text)]
data=data_processed[0]['results']
next_p=data_processed[0]['next']
while(next_p!=None):
    url=next_p
    payload = ""
    headers = {
        'Authorization': "Basic YWRtaW46cGFzc3dvcmQ=",
        'cache-control': "no-cache",
        'Postman-Token': "23423423423423"
        }

    response = requests.get( url, headers=headers)
    data_processed = [json.loads(response.text)]
    data+=data_processed[0]['results']
    next_p=data_processed[0]['next']
    
# data={}
# data['Active Tasks']=1
# results=[]
# for tas in data_processed:
#     temp={}
#     temp['id']=tas['id']
#     temp['name']=tas['name']
#     temp['size']=tas['size']
#     temp['status']=tas['status']
#     temp['labels']=tas['labels']
#     temp['annotation']=annotated
#     results.append(temp)
# data['Task List']=results
tasks=[]
for task in data:
    for i in ['url','size','mode','owner','assignee','bug_tracker','created_date','updated_date','overlap','segment_size','z_order','flipped','segments','status','labels','image_quality']:
        del task[i]
#     temp=[]
#     for i in task['labels']:
#         del i['attributes']
#         temp.append(i)
#     task['labels']=temp
    tasks.append(task)
import json
data=json.dumps(tasks)
formatted_table = json2html.convert(json = data)

print (formatted_table)