# 세 개의 자연수 A, B, C가 주어질 때 A×B×C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.
#
# 예를 들어 A = 150, B = 266, C = 427 이라면
#
# A × B × C = 150 × 266 × 427 = 17037300 이 되고,
#
# 계산한 결과 17037300 에는 0이 3번, 1이 1번, 3이 2번, 7이 2번 쓰였다.
def switch1(x):
    return {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
    }.get(x, -1)
a = input()
b = input()
c = input()

result = int(a) * int(b) * int(c)

array = [0,0,0,0,0,0,0,0,0,0]

result = str(result)

for i in range(len(result)):
    array[switch1(result[i])] += 1

for i in range(len(array)):
    print(array[i])