# -*- Encoding:UTF-8 -*-

# 백준 알고리즘 1629번
# 곱셈
# 입력 : 첫째 줄에 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M이 주어진다.
# 이어서 둘째 줄부터 N개의 줄에 걸쳐 듣도 못한 사람의 이름과,
# N+2째 줄부터 보도 못한 사람의 이름이 순서대로 주어진다.이름은 띄어쓰기 없이 영어 소문자로만 이루어지며,
# 그 길이는 20 이하이다. N, M은 500,000 이하의 자연수이다.
# 출력 : 듣보잡의 수와 그 명단을 사전순으로 출력한다.


N, M = map(int, input().split(" "))

not_listen = []
not_see = []
result = []

for i in range(N):
    not_listen.append(input())

for i in range(M):
    not_see.append(input())

if N > M:
    for i in range(M):
        if not_listen.count(not_see[i]) != 0:
            result.append(not_see[i])
else:
    for i in range(N):
        if not_see.count(not_listen[i]) != 0:
            result.append(not_listen[i])

result.sort()

print(len(result))
for i in range(len(result)):
    print(result[i])

