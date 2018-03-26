# -*- Encoding:UTF-8 -*-

# 백준 알고리즘 1006번
# 습격자 초라기

def find_relation(index):
    relation_list = []

    if index == 0 :
        if circle_1[index] + circle_1[N-1] <= W:
            relation_list.append(N - 1)
    else:
        if circle_1[index] + circle_1[index - 1] <= W:
            relation_list.append(index - 1)

    if index == N-1:
        if circle_1[index] + circle_1[0] <= W:
            relation_list.append(0)
    else:
        if circle_1[index] + circle_1[index + 1] <= W:
            relation_list.append(index + 1)

    if circle_1[index % N] + circle_2[index % N] <= W:
        relation_list.append(index)

    for i in range(len(relation_list)):
        if relation_circle[relation_list[i]] == -1:
            relation_list.remove(relation_list[i])
            i-=1

    return relation_list

test_case = int(input("테스트 케이스의 수 입력 : "))

for i in range(test_case):
    N = int(input("구역의 갯수 : "))
    W = int(input("소대원의 수 : "))

    circle_1 = input("첫째 줄에 배치된 수 : ").split(" ")
    circle_2 = input("둘째 줄에 배치된 수 : ").split(" ")

    circle_1.append(circle_1[0])
    circle_1.insert(0, circle_1[N-1])

    circle_2.append(circle_2[0])
    circle_2.insert(0, circle_2[N - 1])

    for i in range(len(circle_1)):
        circle_1[i] = int(circle_1[i])
        circle_2[i] = int(circle_2[i])

    relation_circle = [0 for i in range(2 * N)]

    print(relation_circle)
    for i in range(1, N + 1):
        if circle_1[i] + circle_1[i-1] <= W:
            relation_circle[i-1] += 1
        if circle_1[i] + circle_2[i] <= W:
            relation_circle[i - 1] += 1
        if circle_1[i] + circle_1[i + 1] <= W:
            relation_circle[i - 1] += 1

        if circle_2[i] + circle_2[i-1] <= W:
            relation_circle[i-1 + N] += 1
        if circle_2[i] + circle_1[i] <= W:
            relation_circle[i - 1 + N] += 1
        if circle_2[i] + circle_2[i + 1] <= W:
            relation_circle[i - 1 + N] += 1

    for i in range(len(relation_circle)):
        if relation_circle[i] == 1:
            temp = find_relation(i)
            if len(temp) is not 0 and relation_circle[temp[0]] == 1:
                relation_circle[i] = -1
                relation_circle[temp[0]] = -1


    print(relation_circle)






