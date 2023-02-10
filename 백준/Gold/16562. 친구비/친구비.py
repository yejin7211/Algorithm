import sys
input = sys.stdin.readline


def find(x):
    if x != root[x]:
        root[x] = find(root[x])
    return root[x]


def union(x, y):
    root[max(x, y)] = min(x, y)


n, m, k = map(int, input().split())
a = list(map(int, input().split()))
root = [i for i in range(n+1)]
for _ in range(m):
    v, w = map(int, input().split())
    union(find(v), find(w))

for i in range(n):
    a[i] = [a[i], i+1]
a.sort()

need_money = 0
friends = set()
for money, person in a:
    if person not in friends:
        person_root = find(person)
        for i in range(1, n+1):
            if find(i) == person_root:
                friends.add(i)
        need_money += money

if k-need_money < 0:
    print('Oh no')
else:
    print(need_money)
