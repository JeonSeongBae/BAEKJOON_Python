# -*- Encoding:UTF-8 -*-

# 백준 알고리즘 1181번

inputString = []
size = int(input())

for i in range(size):
    inputString.append(input())

def strange_sort(strings):
    return sorted(strings, key=lambda strings:(len(strings), strings))

inputString = list(set(inputString))
print(strange_sort(inputString))