s = input().rstrip()
cases = set()
for sIdx in range(len(s)):
    for eIdx in range(sIdx + 1, len(s) + 1):
        cases.add(s[sIdx:eIdx])
print(len(cases))