def replace_code(s):
    s = s.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")
    return s

def solution(m, musicinfos):
    m = replace_code(m)    
    music = dict()
    musicTime = dict()
    for info in musicinfos:
        info = list(info.split(','))
        startT = list(info[0].split(':'))
        endT = list(info[1].split(':'))
        # 음악이 00:00를 넘겨서까지 재생되는 일은 없다.
        startMusic = min(int(startT[0])*60+int(startT[1]), int(endT[0])*60+int(endT[1]))
        endMusic = max(int(startT[0])*60+int(startT[1]), int(endT[0])*60+int(endT[1]))
        time = endMusic - startMusic
        musicTime[info[2]] = time # 음악 재생 시간
        info[3] = replace_code(info[3])
        lyrics = info[3]
        # 음악 길이보다 재생된 시간이 짧을 때는 처음부터 재생 시간만큼만 재생된다.
        if len(lyrics) > time: 
            lyrics = lyrics[0:time]
        elif len(lyrics) < time:
            # 음악 길이보다 재생된 시간이 길 때는 음악이 끊김 없이 처음부터 반복해서 재생된다
            while len(lyrics) < time:
                lyrics += info[3]
        music[info[2]] = lyrics # 음악 가사 길이
    
    listenedMusic = list() # Idx0: 조건이 일치하는 음악 제목, Idx1: 재생 시간
    for title, lyrics in music.items():
        if m in lyrics:
            listenedMusic.append([title, musicTime[title]])
    
    if len(listenedMusic) == 0:
        return "(None)"
    # 조건이 일치하는 음악이 여러 개일 때에는 라디오에서 재생된 시간이 제일 긴 음악 제목을 반환한다. 재생된 시간도 같을 경우 먼저 입력된 음악 제목을 반환한다.
    listenedMusic.sort(key=lambda x:x[1], reverse=True)    
    return listenedMusic[0][0]