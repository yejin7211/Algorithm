import sys
input = sys.stdin.readline

cnt = 0


def recursion(s, l, r):
    global cnt
    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        cnt += 1
        return recursion(s, l+1, r-1)


def isPalindrome(s):
    return recursion(s, 0, len(s)-1)


t = int(input())
for _ in range(t):
    cnt = 0
    s = input().rstrip()
    print(isPalindrome(s), cnt + 1)
