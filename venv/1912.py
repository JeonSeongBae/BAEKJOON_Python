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
    if numbers[0] >= 0:
        plus = True
    else:
        minus = True

    for i in range(N):
        if numbers[i] >= 0 and plus:
            temp += numbers[i]
        elif numbers[i] < 0 and minus:
            temp += numbers[i]
        else:
            if plus:
                plus = False
                minus = True
            else:
                plus = True
                minus = False

            sum_numbers.append(temp)
            temp = numbers[i]
    sum_numbers.append(numbers[N-1])

    temp = 0
    temp_numbers = []
    if sum_numbers[0] < 0:
        index = 1
    else:
        index = 0

    for i in range(index, len(sum_numbers)-1):
        if sum_numbers[i] < 0:
            if sum_numbers[i] + sum_numbers[i+1] > 0:
                temp += sum_numbers[i]
            else:
                temp_numbers.append(temp)
                temp_numbers.append(sum_numbers[i])
                temp = 0
        else:
            temp += sum_numbers[i]
    last = sum_numbers[len(sum_numbers)-1]
    if last < 0:
        temp_numbers.append(temp)
        temp_numbers.append(last)
    else:
        temp_numbers.append(temp + last)

    print(max(temp_numbers))
