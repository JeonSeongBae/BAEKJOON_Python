# -*- Encoding:UTF-8 -*-

# 백준 알고리즘 1912번
# 연속합


def make_array(array):
    if len(array) <= 2:
        return array

    length = int(len(array)/2)
    count = 0
    result = []
    i = 1
    while i < length:
        index = i * 2 + 1
        if array[index - 1] + array[index] > 0 and array[index] + array[index+1] > 0:
            result.append(array[index - 1] + array[index] + array[index + 1])
            i += 2
            count += 1
        else:
            result.append(array[index - 1])
            result.append(array[index])
            if i == length-1:
                result.append(array[index + 1])
            i += 1

    if count is 0:
        return array
    else:
        return make_array(result)


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
    if len(sum_numbers) > 1 and sum_numbers[0] < 0:
        sum_numbers.pop(0)

    if len(sum_numbers) == 0:
        print(max(numbers))
    else:
        print(max(make_array(sum_numbers)))


