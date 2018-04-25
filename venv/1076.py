# -*- Encoding:UTF-8 -*-

# 백준 알고리즘 1076번
# 저항
# 입력 : 첫째 줄에 첫번째 색, 둘째 줄에 두번째 색, 셋째 줄에 세번째 색이 주어진다.
# 출력 : 첫째 줄에 입력을 주어진 저항의 저항값을 출력한다.
import sys


first = sys.stdin.readline().replace("\n", "")
second = sys.stdin.readline().replace("\n", "")
third = sys.stdin.readline().replace("\n", "")

color = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
value = [str(i) for i in range(0, 10)]

result = int(value[color.index(first)] + value[color.index(second)]) * pow(10, int(value[color.index(third)]))
print(result)