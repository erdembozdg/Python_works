# capitalize
from collections import defaultdict

def capitalize1(string):
    return ' '.join(word[0].upper() + word[1:] for word in string.split(" "))

def capitalize2(string):
    li = []
    li.append(string[0].upper())
    for i in range(1, len(string)):
        if string[i-1] == ' ':
            li.append(string[i].upper())
        else:
            li.append(string[i])
    return ''.join(li)
assert capitalize1("erdem bozdag") == capitalize2("erdem bozdag")
