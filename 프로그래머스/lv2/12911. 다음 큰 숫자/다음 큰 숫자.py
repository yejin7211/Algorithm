def solution(n):
    oneCnt = bin(n).count("1")
    while True:
        n += 1 
        if oneCnt == bin(n).count("1"):
            return n