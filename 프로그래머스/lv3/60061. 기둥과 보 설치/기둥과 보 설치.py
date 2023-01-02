def installable(x, y, a, n, pillar, bo):
    possible = False
    if a == 0:  # 기둥
        if y == 0:
            possible = True  # 바닥 위 
        if bo[y][x] or (x-1 >= 0 and bo[y][x-1]):
            possible = True  # 보의 한쪽 끝 위
        if y-1 >= 0 and pillar[y-1][x]:
            possible = True  # 다른 기둥 위
    else:  # 보
        if y-1 >= 0 and (pillar[y-1][x] or (x+1 <= n and pillar[y-1][x+1])):
            possible = True  # 한쪽 끝 부분이 기둥 위
        elif x-1 >= 0 and x+1 <= n and bo[y][x-1] and bo[y][x+1]:  
            possible = True  # 양쪽 끝 부분이 다른 보와 연결
    return possible

def delete(x, y, a, n, pillar, bo):
    if a == 0:  # 기둥
        pillar[y][x] = 0
        for i in range(n+1):
            for j in range(n+1):
                if pillar[i][j] and not installable(j, i, 0, n, pillar, bo):
                    pillar[y][x] = 1
                if bo[i][j] and not installable(j, i, 1, n, pillar, bo):
                    pillar[y][x] = 1
    else:  # 보
        bo[y][x] = 0
        for i in range(n+1):
            for j in range(n+1):
                if pillar[i][j] and not installable(j, i, 0, n, pillar, bo):
                    bo[y][x] = 1
                    break
                if bo[i][j] and not installable(j, i, 1, n, pillar, bo):
                    bo[y][x] = 1
                    break
    return pillar, bo

def solution(n, build_frame):
    answer = []
    
    pillar = [[0 for _ in range(n+1)] for _ in range(n+1)]
    bo = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for x, y, a, b in build_frame:
        if b == 1:  # 설치
            if installable(x, y, a, n, pillar, bo):
                if a == 0:
                    pillar[y][x] = 1
                else:
                    bo[y][x] = 1
        else:  # 삭제
            pillar, bo = delete(x, y, a, n, pillar, bo)
    
    for i in range(n+1):  # 최종 구조물의 상태
        for j in range(n+1):
            if pillar[i][j]:
                answer.append([j, i, 0])
            if bo[i][j]:
                answer.append([j, i, 1])
    answer.sort(key=lambda x:(x[0], x[1], x[2]))
    return answer