import locale


def eval_postfix(pstexpr: str) -> int | float | None:
    S = []
    numstr = []
    lst_e = False
    for ch in pstexpr:
        if ch.isnumeric() or ch == '.' or ch == 'e' or (lst_e and ch == '-'):
            numstr.append(ch)
            if ch == 'e': lst_e = True
            else: lst_e = False
        elif ch in ' -+/*':
            if numstr:
                S.append(locale.atof(''.join(numstr)))
                numstr.clear()
            if ch != ' ':
                rhs, lhs = S.pop(), S.pop()
                if ch == '*': S.append(lhs * rhs)
                elif ch == '-': S.append(lhs - rhs)
                elif ch == '+': S.append(lhs + rhs)
                elif ch == '/': S.append(lhs / rhs)
    return S[-1] if S else None


print(eval_postfix('5 2 3 + 2 5e-1 * * +')) # 55.0
print(eval_postfix('1e-2 1e-2 -'))

