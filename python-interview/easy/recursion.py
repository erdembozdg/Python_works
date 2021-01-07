
def sum_func(n):
    if n<10:
        return n
    return n%10 + sum_func(int(n/10))
print(sum_func(4321))

def word_split(s, li, output = None):
    if output is None:
        output = []
    for i in li:
        if s.startswith(i):
            output.append(i)
            word_split(s[len(i):], li, output)
    return output
print(word_split('ilovedogsJohn',['i','am','a','dogs','lover','love','John']))