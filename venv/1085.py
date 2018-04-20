# -*- Encoding:UTF-8 -*-

# 백준 알고리즘 1085번
# 직사각형에서 탈출


x, y, w, h = map(int, input().split(" "))

print(min(x, w-x, y, h-y))