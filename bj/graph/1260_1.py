"""
1. 문제 이해
    1. 설명
        * dfs, bfs 로 탐색한 결과를 작성
        * 정점의 번호가 작은 것을 먼저 방문, 방문할 점이 없는 경우 종료
    2. 제약사항
        * 1 <= N 정점의 갯수 <= 1,000
        * 1 <= M 간선의 갯수 <= 10,000
2. 접근 방법
    * 그래프는 딕셔너리에 리스트들로 구현
    * dfs 재귀로 구현
    * bfs 큐로 구현
3. 코드 설계
    1. N, M, V 입력
    2. graph 딕셔러니 초기화, M 만큼 반복 입력
        1. 간선 시작 끝 a, b 로 입력
        2. a -> b, b -> a 로 이동할 수 있게 그래프에 추가
    3. dfs, bfs방문 리스트 추가
    4. dfs 함수 정의(현재노드)
        1. 방문 리스트에 현재 노드 추가
        2. 해당 노드에서 연결된 노드들 반복
        3. 방문하지 않았다면 dfs 함수 재귀 호출
    5. bfs 함수 정의
"""
from sys import stdin
from collections import deque

N, M, V = map(int, stdin.readline().split())
graph = {}

for _ in range(M):
    a, b, = map(int, stdin.readline().split())
    if a not in graph:
        graph[a] = []
    if b not in graph:
        graph[b] = []
    graph[a].append(b)
    graph[b].append(a)

for g in graph.values():
    g.sort()

dfs_visited, bfs_visited = [False for _ in range(N + 1)], [False for _ in range(N + 1)]


def dfs(start_v):
    dfs_visited[start_v] = True
    print(start_v, end=' ')
    if start_v not in graph:
        return
    for v in graph[start_v]:
        if dfs_visited[v] is False:
            dfs(v)


dfs(V)
print()


def bfs(start_v):
    bfs_visited[start_v] = True
    queue = deque()
    queue.append(start_v)
    while queue:
        cur_v = queue.popleft()
        print(cur_v, end=' ')
        if start_v not in graph:
            return
        for v in graph[cur_v]:
            if bfs_visited[v] is False:
                bfs_visited[v] = True
                queue.append(v)


bfs(V)