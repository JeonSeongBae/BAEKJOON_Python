# -*- Encoding:UTF-8 -*-

# 백준 알고리즘 1074번
# Z
# 입력 : 첫째 줄에 N r c가 주어진다. N은 15보다 작거나 같은 자연수이고,
# r과 c는 0보다 크거나 같고, 2^N-1보다 작거나 같은 정수이다
# 출력 : 첫째 줄에 문제의 정답을 출력한다.


N, r, c = map(int, input().split(" "))

count = 0

while True:
    if r >= int(2 ** (N - 1)):
        count += int(((2 ** N) ** 2)/2)
        r -= int(2 ** (N - 1))

    if c >= int(2 ** (N - 1)):
        count += int(((2 ** N) ** 2)/4)
        c -= int(2 ** (N - 1))

    if N == 1:
        break
    else:
        N -= 1

print(count)