# -*- Encoding:UTF-8 -*-

# 백준 알고리즘 2914번
# 5와 6의 차이
# 입력 : 첫째 줄에 두 정수 A와 B가 주어진다. (1 <= A,B <= 1,000,000)
# 출력 : 첫째 줄에 상근이가 구할 수 있는 두 수의 합 중 최소값과 최대값을 출력한다.


A, B = input().split(" ")

A = str.replace(A, "5", "6")
B = str.replace(B, "5", "6")

result_max = int(A) + int(B)

A = str.replace(A, "6", "5")
B = str.replace(B, "6", "5")

result_min = int(A) + int(B)

print(result_min, result_max)