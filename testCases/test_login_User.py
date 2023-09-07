import requests
from endpoints import User
import json
from endpoints import reqres



def test_login_user():
    Email_id =User.generateEmail()
    Add_user = User.addUser("micky","cred",Email_id,"Password@123")
    Login_user = User.loginUser(Email_id,"Password@123")
    Get_user = User.getUser(Login_user)
    Logout_user = User.logoutUser(Login_user)
    #Delete_user = User.DeleteUser(Login_user)


def test_post_reqres():
    Email_id = User.generateEmail()


