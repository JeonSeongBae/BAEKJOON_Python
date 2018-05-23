# -*- Encoding:UTF-8 -*-
import sys

# 백준 알고리즘 2004번
# 조합 0의 개수
# 입력 : 첫째 줄에 정수 n, m(0≤m≤n≤2,000,000,000, n!=0)이 들어온다.
# 출력 : 첫째 줄에 0의 개수를 출력한다.


n, m = map(int, input().split(" "))
count_list = [0 for i in range(n+1)]

for i in range(1, n+1):
    count = 0
    temp = i
    while temp % 5 == 0:
        temp = int(temp/5)
        count += 1
    count_list[i] = count

print(count_list)
#
# for i in range(m+1, n+1):
#     temp = i
#     while True:
#         if temp % 5 == 0:
#             count_5 += 1
#             temp = int(temp / 5)
#         else:
#             break
#
# for i in range(1, n-m+1):
#     temp = i
#     while True:
#         if temp % 5 == 0:
#             count_5 -= 1
#             temp = int(temp / 5)
#         else:
#             break
#
# print(count_5)