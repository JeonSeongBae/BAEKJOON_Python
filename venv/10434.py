# -*- Encoding:UTF-8 -*-

# 백준 알고리즘 10434번
# 행복한 소수

def check_happy(num):
    if num == 1:
        return True
    else:
        temp = str(num)
        result = 0
        for i in range(len(temp)):
            result += int(temp[i])**2

        return check_happy(result)

user_input = int(input())
data = []
for i in range(user_input):
    temp = input().split(" ")
    data.append(int(temp[1]))

prime_numbers = [2]

for i in range(3, 10001):
    check = False
    for k in range(0, len(prime_numbers)):
        if i % prime_numbers[k] == 0:
            check = True
    if not check:
        prime_numbers.append(i)

result = []

for i in range(user_input):
    happy = False
    for k in range(len(prime_numbers)):
        if int(data[i]) == prime_numbers[k]:
            happy = True

        if data[i] < prime_numbers[k]:
            break

    if happy:
        if check_happy(data[i]):
            result.append("Yes")
        else:
            result.append("No")
    else:
        result.append("No")

for i in range(user_input):
    print(i+1, data[i], result[i])