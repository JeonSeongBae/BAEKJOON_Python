# -*- Encoding:UTF-8 -*-

# 백준 알고리즘 1057번
# 토너먼트
# 입력 : 첫째 줄에 참가자의 수 N과 1 라운드에서 김지민의 번호와 임한수의 번호가 순서대로 주어진다.
# N은 100,000보다 작거나 같은 자연수이고, 김지민의 번호와 임한수의 번호는 N보다 작거나 같은 자연수이고, 서로 다르다.
# 출력 : 첫째 줄에 김지민과 임한수가 대결하는 라운드 번호를 출력한다. 만약 서로 대결하지 않을 때는 -1을 출력한다.


N, kim, lim = map(int, input().split(" "))

round = 0
while N > 1:
    round += 1
    if max(kim, lim) - min(kim, lim) == 1 and max(kim, lim) % 2 == 0:
        break

    N = int(N / 2) + (N % 2)
    kim = int(kim / 2) + (kim % 2)
    lim = int(lim / 2) + (lim % 2)

print(round)