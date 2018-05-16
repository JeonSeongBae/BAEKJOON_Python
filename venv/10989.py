# -*- Encoding:UTF-8 -*-

# BAEKJOON 10989번
#
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

size = int(input())

arr = []
radix = [[] for i in range(10)]
index = -1

# 입력받기
for i in range(size):
    arr.append(input())

position = len(max(arr))

for j in range(position + 1):
    for i in range(size):
        a = arr.pop(0)
        if(index + len(a) < 0):
            b = 0
        else:
            b = int(a[index])
        radix[b].append(a)
    for i in range(10):
        for k in range(size):
            if(len(radix[i]) == 0):
                break;
            else:
                arr.append(radix[i].pop(0))
    index -= 1

for i in range(len(arr)):
    print(arr[i])