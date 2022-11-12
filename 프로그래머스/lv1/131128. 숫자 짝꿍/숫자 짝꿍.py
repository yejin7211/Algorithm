def solution(X, Y):
    answer = ""
    listX = list(''.join(X))
    listY = list(''.join(Y))
    numsDic = {}
    for c in listY:
        if c in numsDic:
            numsDic[c] += 1
        else:
            numsDic[c] = 1

    listXY = list()
    for c in listX:
        if c in numsDic and numsDic[c] > 0:
            listXY.append(c)
            numsDic[c] -= 1
    if listXY == []:
        return "-1"

    listXY.sort(reverse=True)
    for v in listXY:
        answer += v
    if answer[0] == "0" and "00" in answer:
        return "0"
    return answer
