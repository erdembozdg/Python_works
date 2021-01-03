
def reverse1(string):
    if string is None or len(string) < 2:
        return "Not possible"
    
    backward = []
    for i in range(len(string)-1, -1, -1):
        backward.append(string[i])
    return "".join(backward)

s = "Erdem Bozdag"
print(reverse1(s))
print("".join(reversed(s)))

li = list(s)
li.reverse()
print("".join(li))



