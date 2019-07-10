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
    images=[]
    for l_id in list(label.values()):
        data[l_id]=0
    data['total_objects']=len(result['shapes'])
    for annot in result['shapes']:
        images.append(annot['frame'])
        l_id=annot['label_id']
        cl_name=label[l_id]
        if cl_name not in data.keys():
            data[cl_name]=1
        else:
            data[cl_name]+=1
    noi=len(list(set(images)))
    
    return data,noi


# annotated,noi=get_annot(1)
# val={}
# val['annotated']=0
# val['not_annotated']=0
# for i in annotated.keys():
#     if i =='total_objects':
#         continue
#     if annotated[i]>0:
#         val['annotated']+=1
#     else:
#         val['not_annotated']+=1
import subprocess
import pandas as pd
import sys
output = subprocess.run('printenv | grep PATH_PREFIX', shell=True, stdout=subprocess.PIPE, 
                        universal_newlines=True)

wrksp=output.stdout[12:]
url = "https://c.onepanel.io/"+wrksp+"api/v1/users"
url="http://c.onepanel.io/onepanel-demo/projects/cvat-public-demo/workspaces/cvat-gpu-4/label/api/v1/users"
payload = ""
headers = {
    'Authorization': "Basic YWRtaW46cGFzc3dvcmQ=",
    'cache-control': "no-cache",
    'Postman-Token': "2423423234234234234234234234"
    }

response = requests.request("GET", url, data=payload, headers=headers)
data_processed = json.loads(response.text)

d=data_processed['results'][0]
data={}

# data['first_name']=d['first_name']
# data['last_name']=d['last_name']
data['email']=d['email']
data['last_login']=d['last_login']
# data['images']=str(noi)
# data['c_annotated']=val['annotated']
# data['c_not_annotated']=val['not_annotated']
formatted_table = json2html.convert(json = data)
print (formatted_table)