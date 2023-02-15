import sys
input = sys.stdin.readline


def func(count, s, space):
    if count == 0:
        print(s)
        return

    func(count-1, s+space+s, space * 3)


while True:
    try:
        n = int(input())
        func(n, '-', ' ')
    except:
        break
