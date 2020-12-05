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