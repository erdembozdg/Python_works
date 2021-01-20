# String permutation

def permute(s):
    out = []
    if len(s) == 1:
        out = [s]
    for i,v in enumerate(s):
        for perm in permute(s[:i] + s[i+1:]):
            out += [v + perm]
    return out  
print(permute('abc'))

def twoStrings(s1, s2):
    return 'YES' if set(s1).intersection(set(s2)) else 'NO'
print(twoStrings("hi world", "hello world"))

def alternatingCharacters(word):
    arr = []
    for i in range(len(word) - 1):
        if word[i] == word[i+1]:
            arr.append(i)
    return len(arr)
print(alternatingCharacters("AABAAB"))