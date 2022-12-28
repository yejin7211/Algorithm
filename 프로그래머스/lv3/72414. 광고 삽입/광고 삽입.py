def str_toSeconds(s):  # 문자열을 초 크기로 바꾸기
    h, m, s = s.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)

def seconds_toStr(minutes):  # 초를 문자열로 바꾸기
    T = ['', '', '']
    for i, n in enumerate([3600, 60, 1]):
        T[i] = str(minutes // n)
        while len(T[i]) <= 1:
            T[i] = '0' + T[i]
        minutes %= n
    return ':'.join(T)
    
def solution(play_time, adv_time, logs):
    # 모든 시작과 끝 시간들 초 형태로 바꾸기 & dp 표시
    play_time = str_toSeconds(play_time)
    adv_time = str_toSeconds(adv_time)
    dp = [0 for _ in range(play_time+1)]
    for log in logs:
        start, end = log.split('-')
        dp[str_toSeconds(start)] += 1
        dp[str_toSeconds(end)] -= 1

    # 누적합
    for i in range(1, play_time):
        dp[i] += dp[i-1]
    for i in range(1, play_time):
        dp[i] += dp[i-1]

    # 시청자들의 누적 재생시간이 가장 많은 시각 찾기
    answer = 0
    max_totalTime = dp[adv_time - 1]
    for i in range(adv_time, play_time):
        if max_totalTime < dp[i] - dp[i-adv_time]:
            max_totalTime = dp[i] - dp[i-adv_time]
            answer = i - adv_time + 1
    return seconds_toStr(answer)