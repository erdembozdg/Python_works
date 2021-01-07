
def to_str(byte_or_str):
    if isinstance(byte_or_str, bytes):
        value = byte_or_str.decode('utf-8')
    else:
        value = byte_or_str
    return value

def to_byte(byte_or_str):
    if isinstance(byte_or_str, str):
        value = byte_or_str.encode('utf-8')
    else:
        value = byte_or_str
    return value


def test(values, key):
    found = values.get(key, [2,3,4])
    return found
print(test({'a':1,"b":4}, 'c'))


a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
assert a[:4] == a[0:4]
assert a[-4:] == a[-4:len(a)]
print(a[::-1])
print(a[-2:2:-2])
print(a[-100:100])
b = a[:]
assert b == a and b is not a
b = a
assert b == a and b is a 
a = [1, 2, 3]
assert b != a and b is not a 

for k,v in enumerate(a):
    print('%d: %s\t' % (k, v), end= '')
print()


li1 = [i for i in range(20) if int(i) % 2 == 0]
li2 = list(map(lambda i: i, filter(lambda x: x % 2 == 0, range(20))))
assert li1 == li2
dic = {'Erdem': 1, 'Bozdag': 2}
print({value: key for key, value in dic.items()})
print({len(key) for key in dic.keys()})


matrix = [[1, 2], [3, 4], [5, 6]]
flat = []
flat.extend(i for row in matrix if sum(row) > 3 for i in row if i > 3)
print(flat)
print([[i for i in row if i > 3] for row in matrix if sum(row) > 3])


it = ((str(x), len(x)) for x in open('python-cookbook/files/data.txt'))
print(next(it))


names = ['Cecilla', 'Lise', 'Marie']
letters = [len(name) for name in names]
longest_name = None
max_letter = 0

for name, count in zip(names, letters):
    if count > max_letter:
        max_letter = count
        longest_name = name
print(longest_name)


def else_block(first, last):
    for i in range(first, last):
        print("%d " % i, end='')
        if i == 100:
            break
    else:
        first = last
        last += 10
        else_block(first, last)
        
else_block(1, 10)


import json
def update_file(path):
    handler = open(path, 'r+')
    try:
        data = handler.read()
        ob = json.loads(data)
    except Exception as e:
        return False
    else:
        result = json.dumps(ob)
        handler.seek(0)
        handler.write(result)
        return True
    finally:
        handler.close()    

update_file('python-cookbook/files/data.txt')

