def isBalanced(s):
    open_list = ['(', '[', '{']
    close_list = [')', ']', '}']
    stack = []
    for i in s:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if len(stack) > 0 and stack[-1] == open_list[pos]:
                stack.pop()
            else:
                return "NO"
    return "YES" if not stack else "NO"

print(isBalanced('{(([])[])[]}[]'))
print(isBalanced('{[(])}'))
