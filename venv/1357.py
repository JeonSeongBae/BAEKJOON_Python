# -*- Encoding:UTF-8 -*-

# 백준 알고리즘 1357번
# 뒤집힌 덧셈
# 입력 : 첫째 줄에 수 X와 Y가 주어진다. X와 Y는 1,000보다 작거나 같은 자연수이다.
# 출력 : 첫째 줄에 문제의 정답을 출력한다.


def Rev(T):
    temp = list(str(T))
    temp.reverse()

    return int("".join(temp))


X, Y = input().split(" ")

print(Rev(Rev(X) + Rev(Y)))




