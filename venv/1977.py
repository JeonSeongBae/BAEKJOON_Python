# -*- Encoding:UTF-8 -*-

# 백준 알고리즘 1977번
# 완전 제곱수
# 입력 : 첫째 줄에 M이, 둘째 줄에 N이 주어진다. M과 N은 10000이하의 자연수이며 M은 N보다 같거나 작다.
# 출력 : M이상 N이하의 자연수 중 완전제곱수인 것을 모두 찾아 첫째 줄에 그 합을, 둘째 줄에 그 중 최소값을 출력한다.
# 단, M이상 N이하의 자연수 중 완전제곱수가 없을 경우는 첫째 줄에 -1을 출력한다.
import math

# for i in range(M, N+1):
#     temp = int(math.pow(int(math.sqrt(i)), 2))
#     if temp == i:
#         num.append(i)
M = int(input())
N = int(input())

num = []

if int(int(M ** 0.5) ** 2) == M:
    num.append(M)

for i in range(int(M ** 0.5) + 1, int(N ** 0.5) + 1):
    num.append(int(i ** 2))

if len(num) is 0:
    print(-1)
else:
    print(sum(num), num[0])