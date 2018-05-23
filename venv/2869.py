# -*- Encoding:UTF-8 -*-

# 백준 알고리즘 2869번
# 5와 6의 차이
# 입력 : 첫째 줄에 세 정수 A, B, V가 공백으로 구분되어서 주어진다. (1 ≤ B < A ≤ V ≤ 1,000,000,000)
# 출력 : 첫째 줄에 달팽이가 나무 막대를 모두 올라가는데 며칠이 걸리는지 출력한다.


A, B, V = map(int, input().split(" "))
V -= A

if V % (A - B) == 0:
    count = int(V / (A - B))
else:
    count = int(V / (A - B)) + 1

print(count + 1)

