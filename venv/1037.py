# -*- Encoding:UTF-8 -*-

# 백준 알고리즘 1037번
# 약수


N = int(input())
divisor = [int(i) for i in input().split()]

print(min(divisor) * max(divisor))