# -*- Encoding:UTF-8 -*-

# 백준 알고리즘 1157
# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.
# A == 65 / Z == 90
count = [0]*26
S = str(input()).upper()

for i in range(len(S)):
    count[ord(S[i]) - 65] += 1

max = -1
maxIndex = -1
duplication = False

for i in range(len(count)):
    if max < count[i]:
        duplication = False
        max = count[i]
        maxIndex = i
    elif count[i] is max:
        duplication = True

if duplication:
    print("?")
else:
    print(chr(maxIndex+65))