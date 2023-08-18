import pytest
from apis import Reqres

@pytest.fixture
def test_class_object():
    return Reqres()

def test_init(test_class_object):
    assert(test_class_object.base_url == 'https://reqres.in/')

# @pytest.mark.negative
def test_get_api(test_class_object):
    response = test_class_object.listUsers()
    assert(response != {})
    
def test_get_api_response(test_class_object):
    response = test_class_object.listUsers()
    assert(response["data"][0]["id"] == 7)
    
def test_post_api(test_class_object):
    response = test_class_object.createUser()
    assert(response == 201)