# -*- Encoding:UTF-8 -*-

# 백준 알고리즘 1463번
# 1로 만들기

user_input = int(input())

if 1 <= user_input <= 10**6:
    count = [0 for i in range(user_input+1)]

    for i in range(2, user_input + 1):
        count[i] = count[i-1]+1
        if i % 3 == 0:
            count[i] = min(count[i], count[int(i/3)] + 1)
        if i % 2 == 0:
            count[i] = min(count[i], count[int(i/2)] + 1)

    print(count[user_input])

