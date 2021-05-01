
def permute(s):
    out = []
    if len(s) == 1:
        return s
    else:
        for k, v in enumerate(s):
            for i in permute(s[:k] + s[k+1:]):
                out += [v + i]
    return out

print(permute('abc'))