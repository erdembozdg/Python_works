
def str_reversal1(string):
    li = list(string)
    return ''.join(li[::-1])

def str_reversal2(string):
    reverse = ''
    for i in string:
        reverse = i + reverse
    return reverse

assert str_reversal1("Erdem Bozdag") == str_reversal2("Erdem Bozdag")

def int_reversal(num):
    li = list(str(num))
    reverse = ''.join(li[::-1])
    if num < 0:
        reverse = reverse.replace("-","")
        return int(reverse) * -1
    return reverse

print(int_reversal(-123456789))
