# -*- Encoding:UTF-8 -*-

# 백준 알고리즘 2839번
# 설탕 배달

N = int(input())

temp = N

n_3 = n_5 = 0

while temp > 0:
    if temp == 1 or temp == 2:
        temp = -1
        break

    if temp%5 == 0:
        n_5 = int(temp/5)
        break

    temp -= 3
    n_3 += 1

if temp == -1:
    print(-1)
else:
    print(n_5 + n_3)