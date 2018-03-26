# -*- Encoding:UTF-8 -*-

# 백준 알고리즘 9095번
# 1, 2, 3 더하기
# make by 명

def calc():
    data = [0, 1, 2, 4, 7]

    for i in range(5,11):
        data.append(data[i-1] + data[i-2] + data[i-3])

    return data

test_case = int(input())

case = []
for i in range(test_case):
    case.append(int(input()))

result = calc()

for i in range(test_case):
    print(result[case[i]])








