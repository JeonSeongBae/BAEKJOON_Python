# -*- Encoding:UTF-8 -*-

# 백준 알고리즘 2965번
# 캥거루 세마리
# 입력 : 첫째 줄에 세 캥거루의 초기 위치 A, B, C가 주어진다. (0 < A < B < C < 100)
# 출력 : 캥거루가 최대 몇 번 움직일 수 있는지 출력한다.


A, B, C = map(int, input().split(" "))

count = 0
while True:
    if A + 1 == B == C - 1:
        break

    if B - A > C - B:
        C = B
        B = A + 1
    else:
        A = B
        B = C - 1

    count += 1

print(count)



