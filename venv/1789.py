# -*- Encoding:UTF-8 -*-

# 백준 알고리즘 1789번
# 수들의 합
# 입력 : 첫째 줄에 자연수 S(1≤S≤4,294,967,295)가 주어진다.
# 출력 : 첫째 줄에 자연수 N의 최대값을 출력한다.


S = int(input())

N = int((S * 2) ** 0.5)
total = int(N * (N - 1) / 2)

if S - total >= N:
    print(N)
else:
    print(N - 1)

