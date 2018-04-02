# -*- Encoding:UTF-8 -*-

# 백준 알고리즘 1932번
# 숫자 삼각형

scale = int(input())

triangle = []
result = []

for i in range(1, scale+1):
    triangle.append(input().split(" "))
    result.append([0 for k in range(i)])

result[0][0] = int(triangle[0][0])
for i in range(1, scale):
    for k in range(0, i+1):
        if k == 0:
            result[i][k] = result[i - 1][k] + int(triangle[i][k])
        elif k == i:
            result[i][k] = result[i - 1][k - 1] + int(triangle[i][k])
        else:
            result[i][k] = max(result[i - 1][k - 1], result[i - 1][k]) + int(triangle[i][k])

print(max(result[scale-1]))
