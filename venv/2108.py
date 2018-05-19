# -*- Encoding:UTF-8 -*-

# 백준 알고리즘 2108번
#
# 수를 처리하는 것은 통계학에서 상당히 중요한 일이다. 통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다. 단, N은 홀수라고 가정하자.
#
# 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 범위 : N개의 수들 중 최대값과 최소값의 차이
# N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.
#
from collections import Counter

size = int(input())
array = []
sum = 0
for i in range(0, size):
    array.append(int(input()))
    sum += array[i]
print(int(round(sum / size, 0))) # 산술평균

array.sort()
print(array[int(size/2)]) # 중앙값

cnt = Counter(array)
temp = cnt.most_common()
max = temp[0][1]
freq = []
first = False
second = False
for i in temp:
    if max == i[1]:
        freq.append(int(i[0]))
        if first:
            second = True
        else:
            first = True

if second:
    freq.sort()
    print(freq[1])
else:
    print(freq[0])
print(array[len(array)-1]-array[0])
