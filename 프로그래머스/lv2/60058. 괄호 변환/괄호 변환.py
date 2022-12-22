def func(p):
    # 1
    if len(p) == 0:
        return ''
    
    # 2
    cnts = {'(':0, ')':0}
    for i in range(len(p)):
        cnts[p[i]] += 1
        if cnts['('] == cnts[')']:
            u = p[:i+1]
            v = p[i+1:]
            break

    # 3
    stack = []
    check = 1
    for c in u:
        if c == '(':
            stack.append(c)
        else:
            if not stack:
                check = 0
                break
            stack.pop()
    if check == 1:
        return u + func(v)

    # 4
    s = '(' + func(v) + ')'
    new_u = ''
    values = {'(':')', ')':'('}
    for c in u[1:-1]:
        new_u += values[c]
    return s + new_u
    
def solution(p):
    return func(p)


