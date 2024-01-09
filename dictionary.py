words=set() #We are just checking spelling in speller,so set is better than dict here

def check(word):

    if word.loswer() in words:
        return True
    else:
        return False

def load(dictionary):
    file=open(dictionary,"r")
    for line in file:
        word=line.rstrip()
        words.add(word)
    file.close()
    return True

def size():
    return len(words)

def unload():
    return True