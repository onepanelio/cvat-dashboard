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
    data['total_objects']=len(result['shapes'])
    for annot in result['shapes']:
        l_id=annot['label_id']
        cl_name=label[l_id]
        if cl_name not in data.keys():
            data[cl_name]=1
        else:
            data[cl_name]+=1
    return data

if __name__ == "__main__":
    data=get_annot(1)
    formatted_table = json2html.convert(json = data)
    print (formatted_table)