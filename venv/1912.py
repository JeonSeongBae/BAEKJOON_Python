# -*- Encoding:UTF-8 -*-

# 백준 알고리즘 1912번
# 연속합

N = int(input())
numbers = [int(i) for i in input().split()]

print(numbers)

max_value = 0

for i in range(N):
    temp = 0
    for k in range(i, N):
        temp += numbers[k]

        max_value = max(max_value, temp)

print(max_value)