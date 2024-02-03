import pytest

def test_firstProgram(setup):
    print("Hello")

@pytest.mark.smoke
def test_secondProgram():
    print("namaste")

def test_crossbrowser(crossbrowser):
    print(crossbrowser)




