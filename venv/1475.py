# -*- Encoding:UTF-8 -*-

# 백준 알고리즘 1475번
# 방 번호

N = list(input())
N = [int(i) for i in N]

digit = [0 for i in range(0, 9)]

for i in range(len(N)):
    if N[i] is 6 or N[i] is 9:
        digit[6] += 1
    else:
        digit[N[i]] += 2

print(int(max(digit)/2) + max(digit) % 2)


