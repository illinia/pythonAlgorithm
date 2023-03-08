"""
1. 문제 이해
    1. 그래프 탐색 문제로 탐색시 상하좌우로만 이동이 가능하다
    2. 그래프에서 연결된 노드들 부분이 몇 개인지 구하는 문제
2. 접근 방법
    * bfs, dfs 둘다로 해결해본다
    * 가로 세로 50 이므로 노드의 갯수 최대 2500, 완전 팀색해도 최대 2500^2
    * 탐색 가능한 노드 위치 입력 받고 완전탐색으로 전체 노드 탐색
    * 팀색중에 한번도 방문한 노드를 재방문 하지 않은 경우 카운트 +1
3. 코드 설계
    1. 테스트 케이스 T
    2. 케이스 갯수만큼 반복
    3. 가로 길이 M, 세로길이 N, 배추가 심어져 있는 위치 K 입력, 그래프를 2차원 배열로, 방문 2차원 배열로, 결과값 0으로 초기화
    4. K 만큼 배추 위치 입력
    5. bfs 함수 생성
        1. 이동 가능한 방향(상하좌우) 배열 생성
        2. 큐 생성, 반환값 1로 초기화
        3. 시작 노드로부터 상하좌우 반복
        4. 방문 가능하고 방문하지 않은 경우에만, 방문 확인하고 해당 노드를 큐에 저장
        5. 방문 가능하지만 방문을 이미 한 경우 반환값 0으로 저장
        6. 함수 실행 종료 후 반환값을 결과값에 더하기
    6. dfs 함수 생성
        0. 최초 노드가 방문 불가능 노드이면 0 반환
        1. 이동 가능한 방향(상하좌우) 배열 생성
        2. 해당 노드 방문 체크, 시작 노드로부터 상하좌우 반복
        3. 방문 가능하고 방문하지 않은 경우이면, 방문 확인하고 dfs 재귀 실행
        4. 방문 가능하지만 방문을 이미 한 경우 파라미터 반환값을 0로 저장
        5. 함수 실행 종료 후 반환값을 결과값에 더하기
    7. 결과값 출력
"""

from collections import deque
from sys import stdin
import sys
sys.setrecursionlimit(1000000)
result_list = []
T = int(stdin.readline())
for _ in range(T):
    row, col, K = list(map(int, stdin.readline().split()))
    graph = [[0] * col for _ in range(row)]
    visited = [[False] * col for _ in range(row)]
    result = 0
    for _ in range(K):
        a, b = list(map(int, stdin.readline().split()))
        graph[a][b] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(init_row, init_col):
        if graph[init_row][init_col] == 0 or visited[init_row][init_col]:
            return 0

        queue = deque()
        queue.append((init_row, init_col))

        while queue:
            cur_row, cur_col = queue.popleft()

            for i in range(len(dx)):
                next_row = cur_row + dx[i]
                next_col = cur_col + dy[i]

                if 0 <= next_row < row and 0 <= next_col < col and graph[next_row][next_col] == 1:
                    if not visited[next_row][next_col]:
                        visited[next_row][next_col] = True
                        queue.append((next_row, next_col))
        return 1


    def dfs(init_row, init_col, value):
        visited[init_row][init_col] = True

        for i in range(len(dx)):
            next_row = init_row + dx[i]
            next_col = init_col + dy[i]

            if 0 <= next_row < row and 0 <= next_col < col and graph[next_row][next_col] == 1:
                if not visited[next_row][next_col]:
                    dfs(next_row, next_col, value)
                else:
                    value = 0

    for i in range(row):
        for j in range(col):
            # bfs1 = bfs(i, j)
            # result += bfs1
            if graph[i][j] == 0 or visited[i][j]:
                continue
            value = 1
            dfs(i, j, value)
            result += value
    result_list.append(str(result))

print('\n'.join(result_list))













