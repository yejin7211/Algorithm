T = int(input())

for _ in range(T):
    n = int(input())
    cnt = 0
    while n != 6174:
        n = str(n)
        while len(n) < 4:
            n += '0'
        nums = [n[0], n[1], n[2], n[3]]
        nums.sort(reverse=True)
        maxN = int(''.join(nums))
        nums.sort()
        minN = int(''.join(nums))
        n = maxN - minN
        cnt += 1
    print(cnt)
