import requests
import json

a=open('nma/data.json').read()
a=json.loads(a)
k=1
for i in a['Oppo'].keys():
    pyload=a['Oppo'][i]
    res=requests.post('http://127.0.0.1:8000/add_phone/',json=pyload)
    print(k)
    k+=1

