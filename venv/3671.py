# -*- Encoding:UTF-8 -*-

# 백준 알고리즘 3671번
# 산업 스파이의 편지

testcase = int(input())

case = []
for i in range(testcase):
    case.append(list(input()))

prime_numbers = [2]

for i in range(2, 9876544):
    check = False
    for k in range(0, len(prime_numbers)):
        if i % prime_numbers[k] == 0:
            check = True
    if not check:
        prime_numbers.append(i)
        print(i)

