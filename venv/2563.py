# -*- Encoding:UTF-8 -*-

# 백준 알고리즘 2743번
# 단어 길이재기
# 입력 : 첫째 줄에 색종이의 수가 주어진다. 이어 둘째 줄부터 한 줄에 하나씩 색종이를 붙인 위치가 주어진다.
# 색종이를 붙인 위치는 두 개의 자연수로 주어지는데 첫 번째 자연수는 색종이의 왼쪽 변과 도화지의 왼쪽 변 사이의 거리이고,
# 두 번째 자연수는 색종이의 아래쪽 변과 도화지의 아래쪽 변 사이의 거리이다.
# 색종이의 수는 100 이하이며, 색종이가 도화지 밖으로 나가는 경우는 없다
# 출력 : 첫째 줄에 색종이가 붙은 검은 영역의 넓이를 출력한다.


N = int(input())
paper = []
for i in range(N):
    paper.append(list(input().split()))

big_paper = [[0 for i in range(100)] for k in range(100)]

for i in range(N):
    temp = paper[i]
    for x in range(int(temp[0]), int(temp[0]) + 10):
        for y in range(int(temp[1]), int(temp[1]) + 10):
            big_paper[x][y] = 1

result = 0
for i in range(100):
    result += sum(big_paper[i])

print(result)

