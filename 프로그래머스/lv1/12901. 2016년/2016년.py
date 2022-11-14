def solution(a, b):
    month = {1:5, 2:1, 3:2, 4:5, 5:0, 6:3, 7:5, 8:1, 9:4, 10:6, 11:2, 12:4}
    day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    return day[(month[a] + b - 1) % 7]