def solution(s):
    answer = 0
    
    i = 0
    flag = 0
    while (i < len(s)):
        if flag == 1:
            answer *= 10
        flag = 1
        if '0' <= s[i] <= '9':
            if s[i] == '0':
                answer += 0
            if s[i] == '1':
                answer += 1
            if s[i] == '2':
                answer += 2
            if s[i] == '3':
                answer += 3
            if s[i] == '4':
                answer += 4
            if s[i] == '5':
                answer += 5
            if s[i] == '6':
                answer += 6
            if s[i] == '7':
                answer += 7
            if s[i] == '8':
                answer += 8
            if s[i] == '9':
                answer += 9
            i += 1
        else:
            if s[i] == 'z':
                answer += 0
                i += 4
            elif s[i] == 'o':
                answer += 1
                i += 3
            elif s[i] == 't':
                if s[i + 1] == 'w':
                    answer += 2
                    i += 3
                elif s[i + 1] == 'h':
                    answer += 3
                    i += 5
            elif s[i] == 'f':
                if s[i + 1] == 'o':
                    answer += 4
                    i += 4
                elif s[i + 1] == 'i':
                    answer += 5
                    i += 4
            elif s[i] == 's':
                if s[i + 1] == 'i':
                    answer += 6
                    i += 3
                elif s[i + 1] == 'e':
                    answer += 7
                    i += 5
            elif s[i] == 'e':
                answer += 8
                i += 5
            elif s[i] == 'n':
                answer += 9
                i += 4

    
    return answer