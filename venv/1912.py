# -*- Encoding:UTF-8 -*-

# 백준 알고리즘 1912번
# 연속합

all = int(input())

numbers = list(input().split())

print(numbers)

max_first = 0
max_last = 0

max = 0

sy = []

for i in range(1, all):
    if numbers[i-1] >= 0 and numbers[i] >= 0:
        max += numbers[i]
    else:
        max_last = i
        sy.append([max_first, max_last, max])
        max_first = i
        max = 0
