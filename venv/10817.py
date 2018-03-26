# 세 정수 A, B, C가 주어진다. 이 때, 두 번째로 큰 정수를 출력하는 프로그램을 작성하시오.

import sys

first, second, third = sys.stdin.readline().split()

first = int(first)
second = int(second)
third = int(third)

a = [first, second, third]

a.sort()

print(a[len(a)-2])