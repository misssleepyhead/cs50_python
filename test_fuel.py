from fuel import convert, gauge
import pytest

# Check the input is str and output is int
def test_convertinput():
    assert convert("4/4") == 100
    assert convert("0/4") == 0
    assert convert("3/4") == 75

# raises error
def test_converterror():
    with pytest.raises(ValueError):
        convert("three/four")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

# check input is int and the ouput is str
def test_gauge_output():
    assert gauge(100) == "F"
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(75) == "75%"
