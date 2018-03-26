# Python을 사용하고 있다면, input 대신 sys.stdin.readline을 사용할 수 있다. 단, 이 때는 맨 끝의 개행문자까지 같이 입력받기 때문에 문자열을 저장하고 싶을 경우 .rstrip()을 추가로 해 주는 것이 좋다.

# 또한 입력과 출력 스트림은 별개이므로, 테스트케이스를 전부 입력받아서 저장한 뒤 전부 출력할 필요는 없다. 테스트케이스를 하나 받은 뒤 하나 출력해도 된다. 이 문제는 메모리 제한이 작아서 테스트케이스를 전부 저장할 수 없도록 설계되었다.\
import sys

a = int(sys.stdin.readline())

for i in range(0, a):
    first, second = sys.stdin.readline().split()
    first = int(first)
    second = int(second)
    print(first + second)