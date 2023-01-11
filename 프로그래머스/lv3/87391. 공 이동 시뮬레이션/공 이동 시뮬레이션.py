def solution(n, m, y, x, queries):
    minYX, maxYX = [y, x], [y, x]
    while queries:
        direction, dx = queries.pop()
        if direction == 0:
            maxYX[1] = min(maxYX[1] + dx, m - 1)
            if minYX[1] != 0:
                minYX[1] = minYX[1] + dx
        elif direction == 1:
            minYX[1] = max(minYX[1] - dx, 0)
            if maxYX[1] != m - 1:
                maxYX[1] = maxYX[1] - dx
        elif direction == 2:
            maxYX[0] = min(maxYX[0] + dx, n - 1)
            if minYX[0] != 0:
                minYX[0] = minYX[0] + dx
        else:
            minYX[0] = max(minYX[0] - dx, 0)
            if maxYX[0] != n - 1:
                maxYX[0] = maxYX[0] - dx
        if minYX[0] >= n or maxYX[0] < 0 or minYX[1] >= m or maxYX[1] < 0:
            return 0
    return (maxYX[0] - minYX[0] + 1) * (maxYX[1] - minYX[1] + 1)