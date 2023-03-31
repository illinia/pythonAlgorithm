"""
1. 문제 이해
    1. 설명
        * 트리 루트가 1일 때 각 노드의 부모를 구하기
    2. 제약사항
        * 2 <= N <= 100,000
        * 둘째 줄부터 N-1 개의 줄에 트리상에서 연결된 두 정점이 주어짐
        * N-1 개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 출력
2. 접근 방법
    * 노드 갯수가 100,000 개 이므로 트리 구현시 N*N 크기의 배열을 초기화하면 메모리 초과 뜰듯
    * N+1 개 만큼의 리스트에 빈 리스트를 넣어서 초기화
    * 부모 노드를 출력해야하므로 방문 확인할 때 부모노드를 저장하면 될듯(기본값 0으로하고)
"""
from collections import deque
from sys import stdin
import sys

sys.setrecursionlimit(1000000)

N = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


# def bfs(tree):
#     visited = ['0' for _ in range(N + 1)]
#     queue = deque()
#     queue.append(1)
#
#     while queue:
#         cur_node = queue.popleft()
#
#         for n in graph[cur_node]:
#             if visited[n] == '0':
#                 visited[n] = str(cur_node)
#                 queue.append(n)
#
#     return visited[2:]
#
#
# print('\n'.join(bfs(graph)))


dfs_visited = ['0' for _ in range(N + 1)]


def dfs(cur_node):
    for n in graph[cur_node]:
        if dfs_visited[n] == '0':
            dfs_visited[n] = str(cur_node)
            dfs(n)

dfs(1)
print('\n'.join(dfs_visited[2:]))