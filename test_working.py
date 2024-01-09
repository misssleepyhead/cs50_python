from working import convert
import pytest

def test_valid():
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"

def test_edge():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"

def test_range():
    with pytest.raises(ValueError):
         convert('09:00 AM to 17:00 PM')
    with pytest.raises(ValueError):
         convert('09:60 AM to 07:00 PM')

def test_invalid_format():
    with pytest.raises(ValueError):
         convert('9:00 AM 5:00 PM')



