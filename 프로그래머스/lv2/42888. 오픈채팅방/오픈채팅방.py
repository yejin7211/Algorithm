def solution(record):
    answer = []
    
    result = []
    idInfoDic = {}
    # record 과정
    for act in record:
        act = list(act.split())
        if act[0] == "Enter":
            idInfoDic[act[1]] = act[2]
            result.append(["들어왔습니다.", act[1], act[2]]) # 들어오다, id, 익명 이름        
        elif act[0] == "Leave":
            result.append(["나갔습니다.", act[1], idInfoDic[act[1]]]) # 나가다, id, 익명 이름
        elif act[0] == "Change":
            idInfoDic[act[1]] = act[2]
    
    # 네임 정리
    for li in result:
        li[2] = idInfoDic[li[1]]
        
    # 메시지 완성
    for li in result:
        answer.append(li[2] + "님이 " + li[0])
        
    return answer