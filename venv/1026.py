# -*- Encoding:UTF-8 -*-

# 백준 알고리즘 1026번
# 보물

N = int(input())

temp_A = input().split(" ")
temp_B = input().split(" ")

A = []
B = []
for i in range(N):
    A.append(int(temp_A[i]))
    B.append(int(temp_B[i]))

A.sort()
B.sort()
B.reverse()

result = 0
for i in range(N):
    result += A[i] * B[i]


print(result)