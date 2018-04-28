# -*- Encoding:UTF-8 -*-

# 백준 알고리즘 1075번
# 나누기
# 입력 : 첫째 줄에 N, 둘째 줄에 F가 주어진다.
# N은 100보다 크거나 같고, 2,000,000,000보다 작거나 같은 자연수이다. F는 100보다 작거나 같은 자연수이다.
# 출력 : 첫째 줄에 마지막 두 자리를 모두 출력한다. 한자리이면 앞에 0을 추가해서 두 자리로 만들어야 한다.


N = input()
F = int(input())


N = int(N[0:len(N) - 2])

temp = ((N % F) * 100) % F
if temp != 0:
    temp = F - temp

if temp < 10:
    print("0" + str(temp))
else:
    print(temp)