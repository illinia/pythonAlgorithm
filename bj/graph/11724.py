"""
1. 문제 이해
    * 방향 없는 그래프가 주어졌을 때 연결 요소의 갯수 구하기(연결된 노드 집합의 갯수)
    * 정점의 갯수 N, 간선의 갯수 M (1 <= N <= 1,000, 0 <= M <= N * (N - 1) / 2)
    * 둘째 줄부터 M 개의 줄에 양 끝점 u, v 주어진다. (1 <= u, v <= N, u != v)
2. 접근 방법
    * bfs, dfs 로 그래프를 순회하는데 완전 탐색
    * 탐색중 모든 정점이 최초 방문이면 갯수 +1
    * 한번이라도 방문한 정점을 탐색한다면 +0
3. 코드 설계
    1. N, M 입력, 그래프 딕셔너리로, 방문리스트 딕셔너리로, answer 0으로 초기화
    2. M 만큼 간선 입력, 양방향으로 그래프에 입력
    3. bfs 함수 정의
        1. 큐 생성
        2. 최초 정점 큐에 삽입, 방문 확인
        3. 큐 빌때까지 반복
            1. 큐 popleft, 정점이 방문할 수 있는 정점들 반복
            2. 방문했는지 확인하고 안했으면 방문 확인, 방문할 수 있는 정점을 큐에 삽입
    4. dfs 함수 정의
        1. 정점 방문 확인
        2. 해당 정점이 방문할 수 있는 정점 반복
            1. 방문했는지 확인하고 안했으면 방문 확인, 방문할 수 있는 정점을 dfs 로 탐색

    5. 그래프 완전 탐색
        1. 방문하지 않았고 정점은 있지만 간선이 없다면 방문 확인하고 answer +1
        2. 탐색하고 answer +1
"""

from collections import deque
from sys import stdin
import sys

sys.setrecursionlimit(1000000)

N, M = list(map(int, stdin.readline().split()))
graph = dict()
visit = dict()
answer = 0

for i in range(1, N + 1):
    graph[str(i)] = []

for _ in range(M):
    a, b = list(map(str, stdin.readline().split()))
    graph[a].append(b)

    graph[b].append(a)


# def bfs(init_v):
#     queue = deque()
#     queue.append(init_v)
#     visit[init_v] = True
#
#     while queue:
#         cur_v = queue.popleft()
#
#         for next_v in graph[cur_v]:
#             if next_v not in visit:
#                 visit[next_v] = True
#                 queue.append(next_v)


def dfs(init_v):
    visit[init_v] = True
    for next_v in graph[init_v]:
        if next_v not in visit:
            dfs(next_v)


for key in graph.keys():
    if key not in visit:
        if key in graph and len(graph[key]) == 0:
            visit[key] = True
            answer += 1
        else:
            # bfs(key)
            dfs(key)
            answer += 1
print(answer)
