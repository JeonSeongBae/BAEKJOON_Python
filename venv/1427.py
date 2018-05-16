# -*- Encoding:UTF-8 -*-

# 백준 알고리즘 1427번
#
# 배열을 정렬하는 것은 쉽다. 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.
#

number = input()
array = []

for i in range(0, len(number)):
    array.append(int(number[i]))

array.sort()
array.reverse()

for i in range(0, len(array)):
    print(array[i], end="")