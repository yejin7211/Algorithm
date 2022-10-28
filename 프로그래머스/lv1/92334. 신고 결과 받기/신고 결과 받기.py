def solution(id_list, report, k):
    answer = []
    report = set(report)
    
    # 초기화
    userActed = {} # key: 모든 유저 아이디, value: 각자가 찾은 정지된 ID 개수
    checkedUser = {} # key: 신고받은 사람, value: 신고받은 횟수
    for id in id_list:
        userActed[id] = 0
        checkedUser[id] = 0
    
    # 신고 과정에서 유저벌 몇 번 신고받았는지 카운팅
    connectedUser = [] # idx0: 신고받은 사람, idx1: 신고한 사람 
    for s in report:
        li = list(s.split())
        li.reverse()
        connectedUser.append(li)
        checkedUser[li[0]] += 1
    
    # k번 이상 신고받아 정지된 유저를 신고했던 유저의 활동을 카운팅
    for key, value in checkedUser.items():
        if value >= k:
            for li in connectedUser:
                if li[0] == key:
                    userActed[li[1]] += 1
    
    # 유저별 유저 정지에 기여한 활동 횟수
    for cnt in userActed.values():
        answer.append(cnt)
    
    return answer