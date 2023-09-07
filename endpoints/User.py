import requests
import json
from faker import Faker

def generateEmail():
    faker = Faker()
    return faker.email()


baseUrl = "https://thinking-tester-contact-list.herokuapp.com"
post_Login_user = "/users/login"
post_add_user ="/users"
delete_user = "/users/me"
get_user = "/users/me"
logout_user = "/users/logout"



def addUser(firstname,lastname,email,password):
    data = {"firstName":firstname,"lastName":lastname,"email": email, "password": password}
    res = requests.post(url=baseUrl+post_add_user,json=data)
    print("Headers: ",res.headers)
    print(res.text)
    assert res.status_code == 201,"User not added"
    # capturing a token
    token = res.json().get('token')
    print(f'token add user:{token}')
    print("Status Code for add user:", res.status_code)





def loginUser(email,password):
    data = {"email": email, "password": password}
    response = requests.post(url=baseUrl+post_Login_user, json=data)
    print("Headers: ",response.headers)
    print(response.text)
    assert response.status_code == 200,"User not log in"
    print("Status Code for login user:", response.status_code)
    #caputing the token
    login_token = response.json().get('token')
    print(f'token add user:{login_token}')
    return login_token

def getUser(token):
    headers = {'Authorization' : token}
    respo = requests.get(url=baseUrl+get_user,headers=headers)
    assert respo.status_code == 200, "User details not fetched"
    print("Status Code for get user:", respo.status_code)


def logoutUser(token):
    headers = {'Authorization': token}
    respo = requests.get(url=baseUrl + logout_user, headers=headers)
    assert respo.status_code == 200, "User  not loggedout "
    print("Status Code for get user:", respo.status_code)

def DeleteUser(token):
    headers = {'Authorization': token}
    response = requests.delete(url=baseUrl + delete_user, headers=headers)
    print("Headers: ", response.headers)
    print(response.text)
    assert response.status_code == 200, "User deleted"
    print("Status Code for Delete user:", response.status_code)

