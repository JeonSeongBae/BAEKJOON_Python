# -*- Encoding:UTF-8 -*-

# 백준 알고리즘 1157
# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.
# A == 65 / Z == 90
count = [0 for i in range(26)]
S = str(input()).upper()

for i in range(len(S)):
    count[ord(S[i]) - 65] += 1

max = 0
maxIndex = -1

for i in range(len(count)):
    if max < count[i]:
        max = count[i]
        maxIndex = i

output = chr(maxIndex+65)
count.sort()
count.reverse()
if count[0] is count[1]:
    print("?")
else:
    print(output.upper())