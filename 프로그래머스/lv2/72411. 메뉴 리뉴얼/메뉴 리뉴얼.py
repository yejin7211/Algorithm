from itertools import combinations

def solution(orders, course):
    result = []
    
    # orders 내 모든 문자열들을 각각 문자 리스트로 바꿈
    for i in range(len(orders)):
        menus = [c for c in orders[i]]
        menus.sort()
        orders[i] = menus
    
    # 조건에 부합하는 코스요리 구하기
    for n in course:
        courseDic = {}
        for orderList in combinations(orders, 2): # orders 내 order을 2개씩 꺼낸다.(nC2)
            interMenus = set(orderList[0]) & set(orderList[1]) # 꺼낸 두 order 간 중복 메뉴를 찾는다.
            for course_menus in combinations(interMenus, n): # 중복 메뉴를 메뉴 n개의 코스로 만든다.
                course_menus = list(course_menus)
                course_menus.sort()
                ss = ""
                for menu in course_menus:
                    ss += menu
                if courseDic.get(ss): # 메뉴가 n개인 코스 후보를 담는 딕셔너리에 넣는다.
                    courseDic[ss] += 1
                else:
                    courseDic[ss] = 1
        courseDic = sorted(courseDic.items(), key=lambda x:x[1], reverse=True)
        maxCnt = 0
        for hobo in courseDic:
            if maxCnt == 0:
                result.append(hobo[0])
                maxCnt = hobo[1]    
            else:
                if hobo[1] < maxCnt:
                    break
                else:
                    result.append(hobo[0])
    
    result.sort()
    return result
    