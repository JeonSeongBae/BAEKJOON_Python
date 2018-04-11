# -*- Encoding:UTF-8 -*-

# 백준 알고리즘 5543번
# 상근날드

burger = []
for i in range(3):
    burger.append(int(input()))

drink = []
for i in range(2):
    drink.append(int(input()))

burger.sort()
drink.sort()

print(burger[0] + drink[0] - 50)