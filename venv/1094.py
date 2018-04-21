# -*- Encoding:UTF-8 -*-

# 백준 알고리즘 1094번
# 막대기


X = int(input())

sticks = [64]

pop_index = 0
min_stick = 0
while X != sum(sticks):
    pop_index = sticks.index(min(sticks))

    min_stick = sticks.pop(pop_index)
    min_stick /= 2

    sticks.append(min_stick)

    if X > sum(sticks):
        sticks.append(min_stick)

print(len(sticks))


