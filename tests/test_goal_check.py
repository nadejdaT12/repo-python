import requests
from faker import Faker
from pytest_steps import test_steps

from modules.goal_methods import create_goal, delete_goal, update_goal, get_goal, post_goal_invalid

fake = Faker()
my_headers = {"Authorization": "pk_200589300_JCKLZL75NT02BXJ5IT3H76WVZJO0Q892"}

def test_get_gaols():
    result = requests.get("https://api.clickup.com/api/v2/team/90151257280/goal", headers=my_headers)
    assert result.status_code == 200
    print("Test 1 passed")
    assert result.json()["goals"][0]["name"] == "Goal_2_05052525"



@test_steps("create new goal", "get created goal", "delete created goal")
def test_create_gaol():
    result = create_goal()
    assert result.status_code == 200
    id = result.json()["goal"]["id"]
    name = result.json()["goal"]["name"]
    print(id)
    name = result.json()["goal"]["name"]
    print(name)
    yield
    # print("Test 1 passed")
    # assert result.json()["goal"]["name"] == random_name
    # print("Test 2 passed")
    get_goal(id)
    print(id)
    print(name)
    yield
    delete_goal(id)
    assert result.status_code == 200
    yield

@test_steps("create new goal","update created goal", "get created goal", "delete created goal")
def test_update_gaol():
    result = create_goal()
    id = result.json()["goal"]["id"]
    yield
    update_goal(id)
    assert result.status_code == 200
    name = result.json()["goal"]["name"]
    yield
    get_goal(id)
    print(id)
    yield
    delete_goal(id)
    assert result.status_code == 200
    yield

@test_steps("create new goal", "delete created goal")
def test_delete_gaol():
    result = create_goal()
    id = result.json()["goal"]["id"]
    print(id)
    name = result.json()["goal"]["name"]
    print(name)
    yield
    delete_goal(id)
    assert result.status_code == 200
    yield

@test_steps("create new goal", "get created goal", "delete created goal")
def test_get_gaol():
    result = create_goal()
    id = result.json()["goal"]["id"]
    name = result.json()["goal"]["name"]
    print(id)
    name = result.json()["goal"]["name"]
    print(name)
    yield
    get_goal(id)
    assert result.status_code == 200
    name = result.json()["goal"]["name"]
    print(id)
    name = result.json()["goal"]["name"]
    print(name)
    yield
    delete_goal(id)
    assert result.status_code == 200
    yield

def test_create_gaol_error():
      random_name = fake.first_name()
      body = {
          "name": random_name
      }
      result = requests.post("https://api.clickup.com/api/v2/team/90151257280/goal", headers={"Authorization": "pk_194692916_BFERPF4Z74VSU"}, json=body)
      assert result.status_code == 401
      print(result)

@test_steps("create new goal", "get invalid created goal")
def test_get_gaol_error():
      result = create_goal()
      assert result.status_code == 200
      id = result.json()["goal"]["id"]
      print(id)
      name = result.json()["goal"]["name"]
      print(name)
      yield
      result = requests.get("https://api.clickup.com/api/v2/goal/" + id, headers={"Authorization": "pk_194692916_BFERPF4Z74VSU"})
      assert result.status_code == 401
      yield

def test_post_goal_invalid():
    result = post_goal_invalid()
    assert result.status_code == 401
