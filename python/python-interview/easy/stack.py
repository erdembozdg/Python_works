def isBalanced(s):
    open_list = ['(', '[', '{']
    bracket_map = {"(": ")", "[": "]",  "{": "}"}
    stack = []
    for i in s:
        if i in open_list:
            stack.append(i)
        elif stack and i == bracket_map[stack[-1]]:
            stack.pop()
        else:
            return False
    return stack == []
    
print(isBalanced('{(([])[])[]}[]'))
print(isBalanced('{[(])}'))
