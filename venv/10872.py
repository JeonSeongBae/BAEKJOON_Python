# -*- Encoding:UTF-8 -*-

# 백준 알고리즘 10872번
# 팩토리얼
# 입력 : 첫째 줄에 정수 N(0 ≤ N ≤ 12)가 주어진다.
# 출력 : 첫째 줄에 N!을 출력한다.


N = int(input())

result = 1
for i in range(1, N + 1):
    result *= i

print(result)