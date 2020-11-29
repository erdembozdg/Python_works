
def str_reversal1(string):
    li = list(string)
    return ''.join(li[::-1])

def str_reversal2(string):
    reverse = ''
    for i in string:
        reverse = i + reverse
    return reverse
assert str_reversal1("Erdem Bozdag") == str_reversal2("Erdem Bozdag")

def str_reversal3(s):
    if(len(s)<=1):
        return s
    else:
        m = int(len(s)/2)
        return str_reversal3(s[m:]) + (str_reversal3((s[:m])))
    pass
print(str_reversal3('hello world'))

def str_reversal4(s):
    if len(s) <= 1:
        return s
    return str_reversal4(s[1:]) + s[0]
print(str_reversal4('hello world'))

def int_reversal(num):
    li = list(str(num))
    reverse = ''.join(li[::-1])
    if num < 0:
        reverse = reverse.replace("-","")
        return int(reverse) * -1
    return reverse
print(int_reversal(-123456789))
