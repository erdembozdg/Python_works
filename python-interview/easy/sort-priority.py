
def priority(values, group):
    result = False
    def helper(x):
        nonlocal result
        if x in group:
            result = True
            return (0, x)
        return (1, x)
    values.sort(key=helper)
    return result
values = [8, 3, 1, 2, 5, 7, 6]
result = priority(values, {3, 6, 8, 2})
print(values, result)