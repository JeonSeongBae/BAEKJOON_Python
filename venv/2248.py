# 예제를 보고 별찍는 규칙을 유추한 뒤에 별을 찍어 보세요.

import math

s = ["  *   ", " * *  ", "***** "]

def makeStar(shift):
    c = len(s)
    for i in range(c):
        s.append(s[i]+s[i])
        s[i] = ("   " * shift + s[i] + "   "*shift)

n = int(input())
k = int(math.log(int(n/3),2))
for i in range(k):
    makeStar(int(pow(2,i)))

for i in range(n):
    print(s[i])