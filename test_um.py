from um import count

def test_valid_input():
    assert count("Um, thanks, um...") == 2

def test_words():
    assert count("Umbrella") == 0

def test_input_with_others():
    assert count("Um?") == 1
