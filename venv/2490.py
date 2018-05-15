# -*- Encoding:UTF-8 -*-

# 백준 알고리즘 2490번
# 윷놀이
# 입력 : 첫째 줄부터 셋째 줄까지 각 줄에 각각 한 번 던진 윷짝들의 상태를 나타내는 네 개의 정수(0 또는 1)가  빈칸을 사이에 두고 주어진다.
# 출력 : 첫째 줄부터 셋째 줄까지 한 줄에 하나씩 결과를  도는 A, 개는 B, 걸은 C, 윷은 D, 모는 E로 출력 한다.


def check_ABCDE(user):
    sticks = user.count('0')

    if sticks == 0:
        return 'E'
    elif sticks == 1:
        return 'A'
    elif sticks == 2:
        return 'B'
    elif sticks == 3:
        return 'C'
    else:
        return 'D'


user1 = input()
user2 = input()
user3 = input()

print(check_ABCDE(user1))
print(check_ABCDE(user2))
print(check_ABCDE(user3))