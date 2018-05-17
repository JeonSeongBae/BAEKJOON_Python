# -*- Encoding:UTF-8 -*-

# 백준 알고리즘 4504번
# 배수찾기
# 입력 : 첫째 줄에 n이 주어진다. 다음 줄부터 한 줄에 한 개씩 숫자 목록에 들어있는 숫자가 주어진다. 이 숫자는 0보다 크고, 10,000보다 작다. 숫자 목록은 0으로 끝난다.
# 출력 : 숫자 목록에 있는 숫자가 n의 배수일 경우 인지 아닌지를 구한 뒤 예제 출력처럼 출력한다.


n = int(input())

input_list = []
while True:
    user_input = int(input())
    if user_input == 0:
        break
    else:
        input_list.append(user_input)

for i in range(len(input_list)):
    if input_list[i] % n == 0:
        print(input_list[i], "is a multiple of", str(n) + ".")
    else:
        print(input_list[i], "is NOT a multiple of", str(n) + ".")
