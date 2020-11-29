import re

text = "The person's phone number is 408-555-1234. Call soon!"

pattern = 'phone'
re.search(pattern, text)
re.findall(pattern, text)
for match in re.finditer(pattern, text):
    print(match.span())
    print(match.group())

text = "My telephone number is 408-555-1234"
pattern = re.compile(r'\w{2,3}\s\w{1,}\s\w+\s\w+\s\d+-\d+-\d+')
result = re.search(pattern, text)
print(result.group())
print(re.search(r"man|woman","This woman was here").group())

print(re.findall(r".\S.at","The bat went splat"))
print(re.findall(r"\d$", 'This ends with a number 2'))
print(re.findall(r"^\d", '1 is the loneliness number'))
print(re.findall(r"[^\d,\s]+", 'There are 3 numbers 345, 44 and 22'))
print(' '.join(re.findall(r"[^!.? ]+", 'This is a string! But it has punctuation. How can we remove it?')))
print(re.findall(r"[\w]+-[\w]+", 'Only find the hypen-words and long-ish'))
print(re.search(r"cat(fish|nap)", 'Hello, would you like some catfish?').group())