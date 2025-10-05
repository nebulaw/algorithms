import locale


def eval_infix(infexpr: str) -> int | float | None:
    rnd = [] # operands
    rtr = [] # operators
    numstr = []
    lst_e = False
    for ch in infexpr:
        # print(f"---- current char is {ch} ----")
        if ch.isnumeric() or ch == '.' or ch == 'e' or (lst_e and ch == '-'):
            # print(f'appending {ch} to {"".join(numstr)}')
            numstr.append(ch)
            if ch == 'e': lst_e = True
            else: lst_e = False
        elif ch in ' )-+/*':
            if numstr:
                rnd.append(locale.atof(''.join(numstr)))
                # print(f'numstr cleared at {"".join(numstr)}')
                numstr.clear()
            if ch == ')':
                op = rtr.pop()
                rhs, lhs = rnd.pop(), rnd.pop()
                if op == '*': rnd.append(lhs * rhs)
                elif op == '-': rnd.append(lhs - rhs)
                elif op == '+': rnd.append(lhs + rhs)
                elif op == '/': rnd.append(lhs / rhs)
                # print(f"appended {rhs} {op} {lhs} to operands")
            elif not ch.isspace():
                # print(f"pushed {ch} to operators")
                rtr.append(ch)
    return rnd[-1] if rnd else None


print(eval_infix('(1+((2+3)*(2*5)))')) # 51.0
print(eval_infix('(1+((2+3)*(4*5e-1)))')) # 101.0

