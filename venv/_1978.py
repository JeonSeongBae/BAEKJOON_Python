# -*- Encoding:UTF-8 -*-

# 백준 알고리즘 1978번
# 소수 찾기

user_input = int(input())
data = input().split(" ")
for i in range(len(data)):
    data[i] = int(data[i])

data.sort(reverse=True)
prime_numbers = [2]

for i in range(3, int(data[0])+1):
    check = False
    for k in range(0, len(prime_numbers)):
        if i % prime_numbers[k] == 0:
            check = True

    if not check:
        prime_numbers.append(i)

count = 0
data.sort()
k = 0

for i in range(user_input):
    for j in range(k, len(prime_numbers)):
        if int(data[i]) == int(prime_numbers[j]):
            count += 1
            break
        elif int(data[i]) < int(prime_numbers[j]):
            break
        k += 1

print(count)
