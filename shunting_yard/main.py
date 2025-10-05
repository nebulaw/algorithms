# The Shunting Yard Algorithm authored by Edsger Dijkstra
# is used to convert infix expressions to postfix expressions.

def itop(infexpr):
    pstexpr = []
    S = [] # stack
    P = { o:(p % 3) + 1 for p, o in enumerate(list('-/^+*'))} # precedences
    for ch in infexpr:
        if ch == ' ':
            continue
        if ch not in '+-*/()^':
            pstexpr.append(ch)
        elif ch == '(':
            S.append(ch)
        elif ch == ')':
            while S and S[-1] != '(':
                pstexpr.append(S.pop())
            if S: S.pop()
        elif ch in '+-*/^':
            if not S or S[-1] == '(' or\
                P[S[-1]] < P[ch] or\
                (P[S[-1]] == P[ch] and ch == '^') or\
                S[-1] == '(':
                S.append(ch)
            else:
                while S and (P[ch] < P[S[-1]] or (P[ch] == P[S[-1]] and ch != '^')):
                    pstexpr.append(S.pop())
                S.append(ch)
        # print('S:', S, 'X:', pstexpr)
    while S: pstexpr.append(S.pop())
    return ''.join(pstexpr)


print(itop('A * B + C'))
print(itop('A + B * C'))
print(itop('A * (B + C)'))
print(itop('A - B + C'))
print(itop('A * B ^ C + D'))
print(itop('A * (B + C * D) + E'))


