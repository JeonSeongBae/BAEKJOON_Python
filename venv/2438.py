# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
#
# 하지만, 오른쪽을 기준으로 정렬한 별 (예제 참고)을 출력하시오.
str = input()
number = int(str)
for i in range(0, number):
    for j in range(0, number - i - 1):
        print(' ', end='')
    for j in range(0, i + 1):
        print('*', end='')
    print()