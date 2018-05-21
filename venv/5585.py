# -*- Encoding:UTF-8 -*-

# 백준 알고리즘 5585번
# 거스름돈
# 입력 : 입력은 한줄로 이루어져있고, 타로가 지불할 돈(1 이상 1000미만의 정수) 1개가 쓰여져있다.
# 출력 : 제출할 출력 파일은 1행으로만 되어 있다. 잔돈에 포함된 매수를 출력하시오.


N = int(input())
exchange = 1000 - N

count = 0

count = int(exchange / 500)
exchange = exchange % 500

count += int(exchange / 100)
exchange = exchange % 100

count += int(exchange / 50)
exchange = exchange % 50

count += int(exchange / 10)
exchange = exchange % 10

count += int(exchange / 5)
exchange = exchange % 5

count += int(exchange / 1)
exchange = exchange % 1

print(count)
