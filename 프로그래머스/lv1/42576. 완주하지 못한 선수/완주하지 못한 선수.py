def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    pLen = len(participant)
    cLen = len(completion)
    for i in range(pLen):
        if i >= cLen:
            return participant[i]
        if participant[i] != completion[i]:
            return participant[i]