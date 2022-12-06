def change_str_to_minutes(s): # 문자열은 분으로 바꾸는 함수
    return int(s[:2]) * 60 + int(s[-2:])

def change_minutes_to_str(m): # 분을 문자열로 바꾸는 함수
    Time = [str(m // 60), str(m % 60)]
    for i in range(2):
        if len(Time[i]) == 1:
            Time[i] = '0' + Time[i]
    return Time[0] + ':' + Time[1]

def solution(n, t, m, timetable):
    for i in range(len(timetable)):
        timetable[i] = change_str_to_minutes(timetable[i])
    timetable.sort()
    
    # 마지막 제외 버스가 도착한 시간에 탈 수 있는 사람은 버스를 탄다.
    tableIdx = 0
    bus_arrivalTime = 540
    for _ in range(n-1):
        count = 0
        while tableIdx < len(timetable) and count < m and timetable[tableIdx] <= bus_arrivalTime:
            tableIdx += 1
            count += 1
        bus_arrivalTime += t
    
    # 마지막 버스에서 콘은 자리 여유가 없으니 마지막 사람보다 1분 일찍 줄을 선다.
    if tableIdx+m-1 < len(timetable) and timetable[tableIdx+m-1] <= bus_arrivalTime:
        return change_minutes_to_str(timetable[tableIdx+m-1] - 1)
    # 마지막 버스에서 콘은 자리 여유가 있으니, 버스 시간 정각에 줄을 선다.
    return change_minutes_to_str(bus_arrivalTime)