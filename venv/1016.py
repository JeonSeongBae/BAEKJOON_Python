# -*- Encoding:UTF-8 -*-

# 백준 알고리즘 1016번
# 제곱 ㄴㄴ 수
# 입력 : 첫째 줄에 min과 max가 주어진다. min은 1보다 크거나 같고,
# 1,000,000,000,000보다 작거나 같은 자연수이고,
# max는 min보다 크거나 같고, min+1,000,000보다 작거나 같은 자연수이다.
# 출력 : 첫째 줄에 [min,max]구간에 제곱ㄴㄴ수가 몇 개인지 출력한다.


min_num, max_num = map(int, input().split(" "))

isSqr = [False for i in range(max_num + 2 - min_num)]

for i in range(max_num):
    if i ** 2 > max_num:
        break

    for j in range(max_num):
        index = (i ** 2) * j
        if index > max_num:
            break
        if index >= min_num:
            isSqr[index - min_num] = True

print(isSqr.count(False))