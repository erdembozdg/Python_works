from itertools import permutations

perm = permutations([1, 2, 3])
print(list(perm))

def permute(s):
    out = []
    if len(s) == 1:
        out = [s]
    else:
        for i, v in enumerate(s):
            for perm in permute(s[:i] + s[i+1:]):
                out += [v + perm]
    return out

def word_split(phrase,list_of_words, output = None): 
    if output is None:
        output = []
    for word in list_of_words:
        if phrase.startswith(word):
            output.append(word)
            word_split(phrase[len(word):],list_of_words, output)
    return output
print(word_split('themanran',['the','ran','man']))
print(word_split('ilovedogsJohn',['i','am','a','dogs','lover','love','John']))
