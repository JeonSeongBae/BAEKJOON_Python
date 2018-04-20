# -*- Encoding:UTF-8 -*-

# 백준 알고리즘 1850번
# 최대 공약수


A, B = map(int, input().split(" "))
if A is 0 or A > 19:
    print(0)
    exit(0)
else:
    A = int("1" * A)

if B is 0 or B > 19:
    print(0)
    exit(0)
else:
    B = int("1" * B)

r = [max(A, B), min(A, B)]

print(r)
i = 0
while True:
    r.append(int(r[i] % r[i+1]))
    for k in range(i):
        print(r[k])
    if r[i+2] is 0:
        print(r[i+1])
        exit(0)
    else:
        i += 1
