from collections import deque

def solution(begin, target, words):
    answer = 0
    
    q = deque()
    q.append([begin, 0]) # 단어, 변환 횟수
    visited = [0 for i in range(len(words))]
    while q:
        prev = q[0][0]
        cnt = q[0][1]
        q.popleft()
        for word in words:
            alphas = [c for c in prev]
            changed = 0
            for c in word:
                if c in alphas:
                    alphas.remove(c)
                else:
                    changed += 1
            if changed == 1 and visited[words.index(word)] == 0:
                if word == target:
                    return cnt + 1
                q.append([word, cnt + 1])
                visited[words.index(word)] = 1
                
    return 0