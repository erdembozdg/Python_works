
def reverse1(string):
    reverse = ""
    for i in range(len(string)):
        reverse = reverse + string[len(string)-1-i]
    return reverse

def reverse2(string):
    reverse = ""
    for i in string:
        reverse = i + reverse
    return reverse

def reverse3(string):
    if len(string) == 0:
        return string
    return reverse3(string[1:]) + string[0]

print(reverse1("Erdem Bozdag"))
print(reverse2("Erdem Bozdag"))
print(reverse3("Erdem Bozdag"))
