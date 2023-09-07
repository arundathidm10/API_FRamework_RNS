import yaml
import json
import requests


Post_adduserURl = "https://reqres.in/api/users"
Patch_modifyuser_URL = "https://reqres.in/api/users/2"



def test_create_user():
    adddata = open('/testdata/userdetails.yaml', 'r').read()
    names = yaml.safe_load(adddata)
    print(names["students"])
    response = requests.post(url=Post_adduserURl,data=adddata )
    print("status code : ",response.status_code)
    print(response.url)
    print(response.headers)
    print(response.text)
    print(response.json())


def test_modify_user():
    modifydata = open('/testdata/userdetails.yaml', 'r').read()
    modifynames = yaml.safe_load(modifydata)
    print(modifynames["patchuser"])
    response = requests.patch(url=Patch_modifyuser_URL,data=modifydata)
    print(response.status_code)
    print(response.headers)
    print(response.json())







