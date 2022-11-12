def solution(arr, cmds):
    answer = []
    for cmd in cmds:
        li = []
        for i in range(cmd[0] - 1, cmd[1]):
            li.append(arr[i])
        li.sort()
        answer.append(li[cmd[2] - 1])
    return answer