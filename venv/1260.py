# -*- Encoding:UTF-8 -*-

# 백준 알고리즘 1260번
# DFS, BFS
# 입력 : 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다.
# 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다.
# 출력 : 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다.
# V부터 방문된 점을 순서대로 출력하면 된다.


def dfs():
    stack_1 = []
    stack_2 = []
    visit = [0 for j in range(N)]

    stack_1.append(V - 1)
    result = ""

    while len(stack_1) > 0:
        root = stack_1.pop(len(stack_1) - 1)
        if visit[root] != 1:
            result += str(root + 1) + " "
            visit[root] = 1

            for k in range(N):
                if graph[root][k] == 1 and visit[k] == 0:
                    stack_2.append(k)

            for j in range(len(stack_2)):
                stack_1.append(stack_2.pop(len(stack_2) - 1))

    return result


def bfs():
    queue = []
    visit = [0 for j in range(N)]

    queue.append(V - 1)
    visit[V - 1] = 1

    result = ""
    while len(queue) > 0:
        root = queue.pop(0)
        result += str(root + 1) + " "
        for k in range(N):
            if graph[root][k] == 1 and visit[k] == 0:
                queue.append(k)
                visit[k] = 1

    return result


N, M, V = map(int, input().split(" "))

line_list = []
for i in range(M):
    line_list.append(list(input().split(" ")))

graph = [[0 for i in range(N)] for i in range(N)]

for i in range(M):
    graph[int(line_list[i][0]) - 1][int(line_list[i][1]) - 1] = 1
    graph[int(line_list[i][1]) - 1][int(line_list[i][0]) - 1] = 1

print(dfs())
print(bfs())