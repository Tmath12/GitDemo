import pytest


@pytest.mark.smoke
def test_firstProgram():
    msg = "hello"
    assert msg == "hello", "Test failed because strings do not match"



def test_secondProgram(setup):
    a = 4
    b = 6
    assert a+2 == 6, "Addition do not match"


