# -*- Encoding:UTF-8 -*-

# 백준 알고리즘 2750번
#
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
#

size = int(input())
array = []

for i in range(0, size):
    array.append(int(input()))

for i in range(0, size):
    for j in range(i, size):
        if(array[i] > array[j]):
            temp = array[i]
            array[i] = array[j]
            array[j] = temp

for i in range(0, size):
    print(array[i])