from bank import value

def test_hello():
    assert value("Hello") == 0

def test_hesentence():
    assert value("Hello, Newman") == 0

def test_20():
    assert value("How you doing?") == 20

def test_100():
    assert value("What's up?") == 100
