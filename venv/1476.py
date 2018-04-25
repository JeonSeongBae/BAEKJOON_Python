# -*- Encoding:UTF-8 -*-

# 백준 알고리즘 1476번
# 날짜 계산
# 입력 : 첫째 줄에 세 수 E, S, M이 주어진다. 문제에 나와있는 범위를 지키는 입력만 주어진다.
# 출력 : 첫째 줄에 E S M으로 표시되는 가장 빠른 연도를 출력한다.
# 1 1 1은 항상 1이기 때문에, 정답이 음수가 나오는 경우는 없다.


E, S, M = map(int, input().split(" "))

x = S - 1
while True:
    if (x % 15) + 1 is E and (x % 19) + 1 is M:
        break
    x += 28

print(x + 1)