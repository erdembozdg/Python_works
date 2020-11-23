# Array Chunk
def chunk(l, n):
    for i in range(0, len(l), n):
        yield l[i:i+n]
print(list(chunk([1, 2, 3, 4, 5, 6], 2)))

# Number of vowels
def vowels(string):
    count = 0
    checker = ['a', 'e', 'i', 'o', 'u']
    for i in string:
        if i in checker:
            count += 1
    return count
print(f'String has {vowels("Erdem Bozdag")} vowels')
