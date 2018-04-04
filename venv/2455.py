# -*- Encoding:UTF-8 -*-

# 백준 알고리즘 2455번
# 지능형 기차

train = []
largest = []
for i in range(4):
    train.append(input().split(" "))

largest.append(int(train[0][1]))
largest.append(largest[0] + int(train[1][1]) - int(train[1][0]))
largest.append(largest[1] + int(train[2][1]) - int(train[2][0]))
largest.append(largest[2] + int(train[3][1]) - int(train[3][0]))

print(max(largest))