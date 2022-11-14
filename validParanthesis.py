def isValid(s):
    """
    :type s: str
    :rtype: bool
    """

    openB = {"{", "[", "("}
    stack = []
    map = { ")": "(",
            "}": "{",
            "]": "["}
    
    for c in s:
        if c in openB:
            stack.append(c)
        else:
            if stack: # if len(stack) > 0
                temp = stack.pop()
                if map[c] != temp:
                    return False
            else:
                return False
    
    return not stack

print(isValid("()[]{}"))
print(isValid("(}"))
print(isValid("]"))