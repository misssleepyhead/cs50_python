from twttr import shorten

def test_delvowel():
    assert shorten("twittr") == "twttr"

def test_number():
    assert shorten("cs50") == "cs50"

def test_capitalized():
    assert shorten("Twitter") == "Twttr"

def test_punctuation():
    assert shorten("What's your name?")=="Wht's yr nm?"

def test_capitalvowel():
    assert shorten("ILOVEYOU") == "LVY"
