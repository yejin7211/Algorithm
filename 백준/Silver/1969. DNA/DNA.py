import sys
input = sys.stdin.readline

n, m = map(int, input().split())
strings = []
for _ in range(n):
    strings.append(input().rstrip())

answer = ''
hamming_distance = 0
for i in range(m):
    alpha = [0 for _ in range(26)]
    for k in range(n):
        alpha[ord(strings[k][i])-65] += 1
    maxIdx = alpha.index(max(alpha))
    answer += chr(maxIdx + 65)
    hamming_distance += sum(alpha) - alpha[maxIdx]

print(answer)
print(hamming_distance)