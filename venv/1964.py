# -*- Encoding:UTF-8 -*-

# 백준 알고리즘 1964번
# 오각형, 오각형, 오각형
# 입력 : 첫째 줄에 N(1≤N≤10,000,000)이 주어진다.
# 출력 : 첫째 줄에 N 단계에서 점의 개수를 45678로 나눈 나머지를 출력한다.


N = int(input())
penta_num = 1
result = 1
for i in range(0, N):
    penta_num += 3
    result = (result + penta_num) % 45678

print(result)