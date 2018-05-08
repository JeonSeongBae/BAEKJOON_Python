# -*- Encoding:UTF-8 -*-

# 백준 알고리즘 1629번
# 곱셈
# 입력 : 첫째 줄에 A, B, C가 빈 칸을 사이에 두고 순서대로 주어진다.
# A, B, C는 모두 2,147,483,647 이하의 자연수이다.
# 출력 : 첫째 줄에 A를 B번 곱한 수를 C로 나눈 나머지를 출력한다.


A, B, C = map(int, input().split(" "))
result2 = 1

while True:
    temp = 0
    while True:
        if B % (2 ** temp) == B:
            temp -= 1
            break
        temp += 1

    B = B - (2 ** temp)
    result = A
    for i in range(temp):
        result = (result % C) ** 2

    result2 = ((result2 % C) * (result % C)) % C

    if B == 0:
        break

print(result2)