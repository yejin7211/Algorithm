import sys
input = sys.stdin.readline

t = (int(input()))

def check_cloths(clothes, n):
    for _ in range(n):
        name, type = input().split()
        if type in clothes:
            clothes[type] += 1
        else:
            clothes[type] = 2

for _ in range(t):
    n = int(input())
    clothes = {}
    check_cloths(clothes, n) # (각 종류별 옷들의 개수 + 1)가지를 딕셔너리를 이용하여 구하기
    valueList = list(clothes.values())
    case = 1
    for value in valueList:
        case *= value
    print(case - 1)

'''
1개 -> 2가지
2개 -> 3가지
3개 -> 4가지
4개 -> 
'''