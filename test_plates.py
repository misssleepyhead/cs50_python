from plates import is_valid


def test_len():
    assert is_valid("H") == False
    assert is_valid("CS50123") == False

def test_alnum():
    assert is_valid("PI.314") == False

def test_alpha():
    assert is_valid("C50") == False


def test_zerofirst():
    assert is_valid("CS05") == False


def test_has_valid_number_position():
    assert is_valid("50CS") == False
    assert is_valid("CS50P") == False
