from numb3rs import validate


def test_invalid_ip():
    assert validate("278.5.4.3") == False
    assert validate("512.512.512.512") == False
    assert validate("255.0.0.1000") == False

def test_valid_ip():
    assert validate("255.255.255.255") == True

def test_invalid_input():
    assert validate("cat") == False

def test_allinput():
    assert validate("255.255.255.256") == False
