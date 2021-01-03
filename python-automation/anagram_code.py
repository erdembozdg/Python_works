#clint eastwood" is an anagram of "old west action

def anagram_check1(s1, s2):
    s1 = s1.replace(" ","").lower()
    s2 = s2.replace(" ", "").lower()
    if sorted(s1) == sorted(s2):
        return True
    return False

def anagram_check2(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    check = {}
    
    for s in s1:
        if s in check:
            check[s] += 1
        else:
            check[s] = 1
    
    for s in s2:
        if s in check:
            check[s] -= 1
        else:
            check[s] = 1
            
    for i in check:
        if check[i] == 1:
            return False
    return True

assert anagram_check1("clint eastwood", "old west action") == anagram_check2("clint eastwood", "old west action")
