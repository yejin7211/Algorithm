from itertools import permutations

def sameID(id1, id2):
    for i in range(len(id2)):
        if id2[i] != '*' and id1[i] != id2[i]:
            return False
    return True
    
def solution(userID_list, bannedID_list):
    answer = 0
    banned_userID_list = []
    for bannedID in bannedID_list:
        userIDs = []
        for userID in userID_list:
            if len(userID)==len(bannedID) and sameID(userID, bannedID):
                userIDs.append(userID)
        banned_userID_list.append(userIDs)
    
    banned_cases = []
    for li in permutations(userID_list, len(banned_userID_list)):
        flag = True
        for i in range(len(li)):
            if li[i] not in banned_userID_list[i]:
                flag = False
                break
        if flag and set(li) not in banned_cases:
            answer += 1
            banned_cases.append(set(li))
    return answer