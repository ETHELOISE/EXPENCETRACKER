//import json
import requests
from .constants import SERVER_URL

class User:
    ENDPOINT = "/user/"

    def __init__(self, user_name=None, email=None , tel_num=None , password=None ):
        self.user_name=user_name
        self.email=email
        self.tel_num=tel_num
        self.password=password

    def save(self):
        url = f"{SERVER_URL}{self.ENDPOINT}"

        payload = {
        'user_name':self.user_name,
        'email':self.email,
        'tel_num':self.tel_num,
        'password':self.password,
        }
    
        headers = {}

        response = requests.request("POST", url, headers=headers, data=payload)

        data = json.loads(response.text)
        self.id = data['id']
            
    def read(id=None):
        url = f"{SERVER_URL}{__class__.ENDPOINT}"
        url += id if id else ''

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        response = json.loads(response.text)

        if id:
            user = __class__(**response)
            return user
        else:
            users = []

            for result in response:
                user = __class__(**result)
                users.append(user)
            
            return users

    def delete(self ,id=None):
        url = f"{SERVER_URL}{self.ENDPOINT}{self.id}"

        payload, headers = {}, {}

        response = requests.request("DELETE", url, headers=headers, data=payload)

        try:
            response.raise_for_status()

            self.id = None
        except Exception:
            raise Exception