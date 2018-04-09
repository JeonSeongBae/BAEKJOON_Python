# -*- Encoding:UTF-8 -*-

# 백준 알고리즘 11053번
# 가장 긴 증가하는 부분 수열

A = int(input())
temp = input().split(" ")

A_i = []
for i in range(A):
    A_i.append(int(temp[i]))

A_i.append(0)

d = [1 for i in range(A+1)]
max_num = 1

for i in range(1, A+1):
    for j in range(i):
        if A_i[j] < A_i[i]:
            if d[i] <= d[j] + 1:
                d[i] = d[j] + 1
                if max_num < d[i]:
                    max_num = d[i]

print(max_num)


