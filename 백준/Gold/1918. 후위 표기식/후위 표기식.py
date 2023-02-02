import sys
input = sys.stdin.readline

s = input().rstrip()

res = []
calc = []
for v in s:
    if v.isalpha():
        res.append(v)
    else:
        if v in ['+', '-']:
            while calc and calc[-1] != '(':
                a = res.pop()
                b = res.pop()
                c = calc.pop()
                res.append(b+a+c)
            calc.append(v)
        elif v in ['*', '/']:
            while calc and calc[-1] in ['*', '/']:
                a = res.pop()
                b = res.pop()
                c = calc.pop()
                res.append(b+a+c)
            calc.append(v)
        elif v == '(':
            calc.append(v)
        elif v == ')':
            while calc[-1] != '(':
                a = res.pop()
                b = res.pop()
                c = calc.pop()
                res.append(b+a+c)
            calc.pop()

while calc:
    a = res.pop()
    b = res.pop()
    c = calc.pop()
    while c == '(':
        c = calc.pop()
    res.append(b + a + c)

print(*res)
