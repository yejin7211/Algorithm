def changeX(x):
    cnt = 0
    stack = []
    for v in x:
        if v == '1':
            stack.append(v)
        else:
            if len(stack) >= 2 and stack[-2] == '1' and stack[-1] == '1':
                stack.pop()
                stack.pop()
                cnt += 1
            else:
                stack.append('0')
    
    res = ''
    x = ''.join(stack)
    for i in range(len(x)-1, -1, -1):
        if x[i] == '0':
            res = x[:i+1]
            for _ in range(cnt):
                res += '110'
            res += x[i+1:]
            break

    if res == '':
        for _ in range(cnt):
            res += '110'
        res += x
    return res
    
def solution(s):
    answer = []
    for x in s:
        res = changeX(x)
        answer.append(res)
    return answer