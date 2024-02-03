import pytest



@pytest.fixture(scope= "class" )
def setup():
    print("I will be executed first")
    yield
    print("I will be executed last")

@pytest.fixture()
def dataload():
    print("user profile data is being created")
    return ["Rahul","shetty","rahulshettyacademy.com"]

@pytest.fixture(params=[("chrome", "Rahul","shetty"), ("firefox", "Rahul"), "IE"])
def crossbrowser(request): #request is used when we have fixture with some value elements
    return request.param