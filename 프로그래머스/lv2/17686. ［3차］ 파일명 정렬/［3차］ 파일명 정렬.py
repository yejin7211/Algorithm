def solution(files):
    answer = []
    for file in files:
        sNumIdx, eNumIdx = -1, -1
        for i in range(len(file)):
            if file[i].isdigit():
                sNumIdx = i
                while file[i].isdigit() and i < len(file):
                    i += 1
                    if i == len(file):
                        break
                eNumIdx = i
                break
        answer.append([file[:sNumIdx], file[sNumIdx:eNumIdx], file[eNumIdx:]])

    answer.sort(key=lambda x:(x[0].upper(), int(x[1])))
    answer = ["".join(i) for i in answer]
    return answer