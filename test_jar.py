from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar.capacity == 12


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    assert jar._size == 0
    jar.deposit(5)
    assert jar._size == 5


def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(5)
    assert jar._size == 5
    jar.withdraw(3)
    assert jar._size == 2

    with pytest.raises(ValueError):
        jar.withdraw(10)
        assert str(ValueError.value) == "Not enough cookies!"
