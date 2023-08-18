import requests
import json


class Reqres:
    def __init__(self):
        self.base_url = 'https://reqres.in/'
    
    def listUsers(self):
        endpoint = 'api/users?page=2'
        api = self.base_url + endpoint
        print(api)
        response = requests.get(api)
        print(response)
        if response.status_code == 200:
            return json.loads(response.text)
        return None
    
    def createUser(self):
        endpoint = 'api/users'
        api = self.base_url + endpoint
        body = {"name": "morpheus","job": "leader"}
        response = requests.post(api, data=body)
        return response.status_code
        

if __name__ == "__main__":
    print(Reqres().listUsers())