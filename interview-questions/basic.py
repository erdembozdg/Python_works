# Fibonacci sequence
def fib(num):
    if num <= 0:
        print("Incorrect number")
    
    elif num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        return fib(num - 1) + fib(num -2)

print(fib(9))

# Fizzbuzz
def fizzbuzz(n):
    for n in range(1, n):
        if n % 3 and n % 5:
            string = "FizzBuzz"
        elif n%3 == 0:
            string = "Fizz"
        elif n%5 == 0:
            string = "Buzz" 
        else:
            string = str(n)
        print(string, end=" ")
    return ""

print(fizzbuzz(21))

# prime numbers
def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(f'{num} is not a prime number')
                break
        else:
            print(f'{num} is a prime number')
    else:
        print(f'{num} is not a prime number')

for i in range(7):
    is_prime(i)

# String Reversal
def reverse1(string):
    arr = list(string)
    print(''.join(arr[::-1]))

def reverse2(string):
    reverse = ''
    for i in list(string):
        reverse = i + reverse
    print(reverse)

reverse1("Erdem Bozdag")
reverse2("Erdem Bozdag")

# Integer Reversal
def reverse_num(num):
    reverse = list(str(num))
    reverse = ''.join(reverse[::-1])
    if num < 0:
        reverse = reverse.replace('-', '')
        print(int(reverse) * -1)
    else:
        print(int(reverse))
    
reverse_num(-12345677)

# Max Character
from collections import defaultdict
def max_char1(string):
    charMap = defaultdict(int)
    for i in list(string):
        charMap[i] = 1 if charMap[i] is None else charMap[i] + 1
    
    maximum = 0
    for key, value in charMap.items():
        if maximum < value:
            maximum = value
            max_ch = key

    print(f"Maximum character is {max_ch}:{maximum}")

def max_char2(string):
    maximum = 0
    max_ch = None
    for i in set(string):
        count = string.count(i)
        if maximum < count:
            maximum = count
            max_ch = i

    print(f"Maximum character is {max_ch}:{maximum}") 

max_char1("Hello World!!")
max_char2("Hello World!!")

# Array Chunk
def chunk(l, n):
    for i in range(0, len(l), n):
        yield l[i:i+n]

print(list(chunk([1,2,4,5,67,7], 2)))

# Anagrams
def build_map(string):
    char_map = defaultdict(int)
    for i in list(string.replace(" ", "").lower()):
        char_map[i] = 1 if char_map[i] is None else char_map[i] + 1
    return char_map

def anagram(s1, s2):
    s1_map = build_map(s1)
    s2_map = build_map(s2)

    if len(s1_map.keys()) != len(s2_map.keys()):
        return False

    for i in s1_map:
        if s1_map[i] != s2_map[i]:
            return False
    return True

s1 = "erdem bozdag"
s2 =  "Erdem Bozdag"
if(anagram(s1, s2)):
    print(f"{s1} {s2} are anagrams")
else:
    print(f"{s1} {s2} are not anagrams")

# Capitalize
def capitalize1(string):
    print(' '.join(word[0].upper() + word[1:] for word in string.split(' ')))

def capitalize2(string):
    li_string = []
    li_string.append(string[0].upper())
    for i in range(1,len(string)):
        if string[i-1] == ' ':
            li_string.append(string[i].upper())
        else:
            li_string.append(string[i])
    print(''.join(li_string))
        
capitalize1("erdem bozdag")
capitalize2("erdem bozdag")

# Number of vovwels
def vowels(string):
    count = 0
    checker = ['a', 'e', 'i', 'o', 'u']
    for i in list(string.lower()):
        if i in checker:
            count += 1
    print(f'String has {count} vowels')

vowels('Erdem Bozdag')
    
        
