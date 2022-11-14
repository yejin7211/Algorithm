def solution(s):
    answer = ''
    i = 0
    while i < len(s):
        if s[i].isdigit():
            answer += s[i]
            i += 1
            while i < len(s) and s[i].isalpha():
                answer += s[i].lower()
                i += 1
        elif s[i].isalpha():
            answer += s[i].upper()
            i += 1
            while i < len(s) and s[i].isalpha():
                answer += s[i].lower()
                i += 1
        elif s[i] == ' ':
            answer += ' '
            i += 1
    return answer