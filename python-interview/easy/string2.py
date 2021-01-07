def alternatingCharacters(word):
    arr = []
    for i in range(len(word) - 1):
        if word[i] == word[i+1]:
            arr.append(i)
    return len(arr)
print(alternatingCharacters("AAABBB"))

def commonChild(s1, s2):
    m = [[0]*(len(s2)+1) for _ in range(len(s1)+1)]
    for i,c in enumerate(s1,1):
        for j,d in enumerate(s2,1):
            if c == d:
                m[i][j] = m[i-1][j-1]+1
            else:
                m[i][j] = max(m[i][j-1],m[i-1][j])
                   
    return m[-1][-1]
print(commonChild("HARRY", "SALLY"))

def check_sos(s):
    s = s.strip()
    return sum(1 for i in range(len(s)) if s[i] != "SOS"[i%3])
print(check_sos("SOSSPSSQSSOR"))

def hackerrankInString(s):
    hr = list("hackerrank")
    for i in s:
        if i == hr[0]:
            hr.pop(0)
    if len(hr) == 0:
        return "YES"
    return "NO"
print(hackerrankInString("hhhhaaaaackkkkerrrrrrrrank"))

arr = [1,2,34,4,5,6]
for i in range(len(arr)):
    print(i,arr[i])