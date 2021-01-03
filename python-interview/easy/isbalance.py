
def isbalance(arr):
    open_list = ['(', '{', '[']
    closed_list = [')', '}', ']']
    
    stack = []
    for i in arr:
        if i in open_list:
            stack.append(i) 
        elif i in closed_list:
            pos = closed_list.index(i)
            if len(stack) > 0 and stack[-1] == open_list[pos]:
                stack.pop()
            else:
                return "No"
    return "Yes" if not stack else "No"          
print(isbalance("{(([])[])[]}[]"))
