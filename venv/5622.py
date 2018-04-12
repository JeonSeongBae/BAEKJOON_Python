# -*- Encoding:UTF-8 -*-

# 백준 알고리즘 5622번
# 다이얼

number = [0 for i in range(ord('Z') + 1)]
number[ord('A')] = number[ord('B')] = number[ord('C')] = 3
number[ord('D')] = number[ord('E')] = number[ord('F')] = 4
number[ord('G')] = number[ord('H')] = number[ord('I')] = 5
number[ord('J')] = number[ord('K')] = number[ord('L')] = 6
number[ord('M')] = number[ord('N')] = number[ord('O')] = 7
number[ord('P')] = number[ord('Q')] = number[ord('R')] = number[ord('S')] = 8
number[ord('T')] = number[ord('U')] = number[ord('V')] = 9
number[ord('W')] = number[ord('X')] = number[ord('Y')] = number[ord('Z')] = 10
number[ord('1')] = 2
number[ord('0')] = 11

tel = input()
tel = list(tel)

time = 0
for i in range(len(tel)):
    time += number[ord(tel[i])]

print(time)
