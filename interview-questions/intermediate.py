
# Printing Steps
def steps1(rows):
    cols = 1
    for r in range(rows):
        cols += 1
        for c in range(cols):
            if c <= r:
                print("#", end='')
            else:
                print(" ", end='')
        print()

def steps2(n, row = 0, string = ''):
    if n == row:
        return
    if n == len(string):
        print(string)
        return steps2(n, row + 1)
    if len(string) <= row:
        string += "#"
    else:
        string += " "
    
    steps2(n,  row, string)


steps1(5)
steps2(5)

# Triangle
print("Print equilateral triangle Pyramid using stars ")
size = 7
m = (2 * size) - 2
for i in range(0, size):
    for j in range(0, m):
        print(end=" ")
    m = m - 1  # decrementing m after each loop
    for j in range(0, i + 1):
        # printing full Triangle pyramid using stars
        print("* ", end=' ')
    print(" ")

