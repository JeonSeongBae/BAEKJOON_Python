# -*- Encoding:UTF-8 -*-

# 백준 알고리즘 1076번
# 저항
# 입력 : 첫째 줄에 수빈이가 이동하려고 하는 채널 N (0 ≤ N ≤ 500,000)이 주어진다.
# 둘째 줄에는 고장난 버튼의 개수 M (0 ≤ M ≤ 10)이 주어진다.
# 고장난 버튼이 있는 경우에는 셋째 줄에는 고장난 버튼이 주어지며, 같은 버튼이 중복되서 주어지는 경우는 없다.
# 출력 : 첫째 줄에 채널 N으로 이동하기 위해 버튼을 최소 몇 번 눌러야 하는지를 출력한다.


N = input()
M = int(input())
trouble = list(input().split(" "))
not_trouble = []
for i in range(10):
    if trouble.count(str(i)) == 0:
        not_trouble.append(i)

equal_num = 0


