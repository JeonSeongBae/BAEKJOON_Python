# -*- Encoding:UTF-8 -*-

# 백준 알고리즘 1912번
# 연속합

N = int(input())
numbers = [int(i) for i in input().split()]

max_value = 0
smallest_num = min(numbers)

sum_numbers = []

plus = False
minus = False

temp = 0

# 1) 음수가 없을 때
if smallest_num >= 0:
    print(sum(numbers))
# 2) 음수가 있을 때
else:
    plus = 0
    minus = 0

    for i in range(N):
        if numbers[i] > 0:
            plus += numbers[i]
            if minus != 0:
                sum_numbers.append(minus)
                minus = 0
        else:
            minus += numbers[i]
            if plus != 0:
                sum_numbers.append(plus)
                plus = 0

    if plus != 0:
        sum_numbers.append(plus)
    if sum_numbers[0] < 0:
        sum_numbers.pop(0)

    total = sum(sum_numbers)

    array = []

    temp = 0
    temp_numbers = []
    temp_2 = 0
    for i in range(0, int(len(sum_numbers)/2)):
        temp = 0
        temp_numbers.append(0)
        for k in range(i, int(len(sum_numbers)/2)):
            temp_2 = temp_numbers[i] + sum_numbers[k] + sum_numbers[k + 1]
            if temp_numbers[i] < temp_2:
                temp_numbers[i] = temp_2

    temp_numbers.append(sum_numbers[len(sum_numbers)-1])
    print(max_value(temp_numbers))


