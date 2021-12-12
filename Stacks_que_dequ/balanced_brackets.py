
def balance_check(s):
    if len(s) % 2 != 0:
        return False
    opening = set('([{')
    matches = set([('(', ')'), ('[', ']'), ('{', '}')])
    stack = []
    for paren in s:
        if paren in opening:
            stack.append(paren)
        else:
            if(len(stack)) == 0:
                return False
            last_opening = stack.pop()
            if (last_opening, paren) not in matches:
                return False
    return len(stack) == 0


print(Balance_check('()'))
