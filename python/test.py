

s = "erdem bozdag"

def reverse(s):
    li = list(s)
    reverse = ''
    for i in li:
        reverse = i + reverse
    return reverse

print(reverse(s))