x = int(input())

sticks = [64]

while x < sum(sticks):
    sticks.sort()
    divided_stick = sticks[0] // 2
    del sticks[0]
    if divided_stick + sum(sticks) >= x:
        sticks.append(divided_stick)
    else:
        sticks.append(divided_stick)
        sticks.append(divided_stick)

print(len(sticks))