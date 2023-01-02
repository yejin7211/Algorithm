def solution(storey):
    answer = 0
    s = str(storey)
    i = 0
    while i < len(s):
        if int(s[i]) < 5:
            answer += int(s[i])
            i += 1
            continue
        cnt = 0
        while i < len(s) and int(s[i]) >= 5:
            cnt += 1
            i += 1
        if cnt == 1 and s[i-1] == '5':
            answer += 5
        else:
            answer += 1
            for j in range(i-cnt, i):
                if j == i-1:
                    answer += 10 - int(s[j])
                else:
                    answer += 9 - int(s[j])
    return answer