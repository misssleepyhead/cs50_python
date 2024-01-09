from seasons import get_min, valid_format
import pytest

def test_invalid_format():
    def test_input():
     with pytest.raises(TypeError):
         valid_format(12-12-2012) == 'Invalid Date'
    # assert valid_format("1996/09/09") == "Invalid Date"
#     with pytest.raises(ValueError):
#         valid_format("1996/09/05")
#     with pytest.raises(ValueError):
#         valid_format("april 9, 2020")



