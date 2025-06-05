import requests
from faker import Faker
fake = Faker()
my_headers = {"Authorization": "pk_200589300_JCKLZL75NT02BXJ5IT3H76WVZJO0Q892"}
def create_goal():
    random_name = fake.first_name()
    body = {
        "name": random_name
    }
    result = requests.post("https://api.clickup.com/api/v2/team/90151257280/goal", headers=my_headers, json=body)
    print(result)
    return result

def update_goal(id):
    random_name_for_update = fake.first_name()
    body = {
        "name": random_name_for_update
    }
    result = requests.put("https://api.clickup.com/api/v2/goal/" + id, headers=my_headers, json=body)
    print(result)
    return result

def delete_goal(id):
    result = requests.delete("https://api.clickup.com/api/v2/goal/" + id, headers=my_headers)
    print(result)
    return result

def get_goal(id):
    result = requests.get("https://api.clickup.com/api/v2/goal/" + id, headers=my_headers)
    print(result)
    return result
