def solution(people, limit):
    answer = 0
    people.sort()
    sIdx, eIdx = 0, len(people) - 1
    while sIdx <= eIdx:
        if people[sIdx] + people[eIdx] <= limit:
            sIdx += 1
        eIdx -= 1
        answer += 1
    return answer