# We are doing delimiter matching when we check to see
# if the parentheses in an expression is balanced

def get_missing_bracket(expr: str) -> str:
    # stack
    S = []
    # closing to opening bracket mapping
    cto = { ')': '(', ']': '[', '}': '{' }
    otc = { k: v for v, k in cto.items() }
    for ch in expr:
        # if opening bracket, push to stack
        if ch in '([{':
            S.append(ch)
        elif ch in ')]}':
            # if stack is empty, return the
            # corresponding opening bracket
            if len(S) == 0:
                return cto[ch]
            # else pop
            elif S[-1] == cto[ch]:
                S.pop()

    return otc[S[-1]] if len(S) > 0 else '*'

# test
print('missing bracket:', get_missing_bracket('2 * ([3 + 5'))

