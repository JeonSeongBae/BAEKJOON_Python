# -*- Encoding:UTF-8 -*-

# 백준 알고리즘 1978번
# 소수 찾기

# 값 입력받기
start = int(input())
end = int(input())
size = end - start

# data에 값을 저장
data = []
for i in range(start, end + 1):
    data.append(i)

# Prime Number를 저장하기 위한 공간
primeList = []

# int형으로 저장
for i in range(len(data)):
    data[i] = int(data[i])

# 소수인지 확인하는 변수
count = 0

# data 리스트 전체 반복
for i in data:
    # 1의 경우 소수가 아님
    if i is 1:
        continue

    # 2의 경우 소수
    if i is 2:
        count += 1
        primeList.append(i)
        continue

    # 2부터 i-1까지 나눠지는 수가 없으면 소수
    for j in range(2, i):
        # j로 나눠진다면 소수
        if i % j == 0:
            break
        elif (j+1) is i:
            count += 1
            primeList.append(i)
            break

# 소수의 합을 출력
total = 0
for i in primeList:
    total += i

if count is 0:
    print("-1")
else:
    print(int(total))
    print(int(primeList[0]))