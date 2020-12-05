# Anagrams
from collections import defaultdict, Counter
def anagram(s1, s2):
    def build_map(string):
        map_char = defaultdict(int)
        for i in list(string.replace(" ", "").lower()):
            map_char[i] = 1 if map_char[i] is None else map_char[i] + 1
        return map_char

    s1_map = build_map(s1)
    s2_map = build_map(s2)

    if len(s1_map.keys()) != len(s2_map.keys()):
        return False

    for i in s1_map:
        if s1_map[i] != s2_map[i]:
            return False
    return True

def makeAnagram(a, b):
    ct_a = Counter(a)
    ct_b = Counter(b)
    ct_a.subtract(ct_b)
    return sum(abs(i) for i in ct_a.values())

s1 = "erdem bozdag"
s2 =  "Erdem Bozdag"
if(anagram(s1, s2)):
    print(f"{s1} {s2} are anagrams")
else:
    print(f"{s1} {s2} are not anagrams")
    
print(makeAnagram(s1, s2))
