"""
1. 문제 이해
    1. 설명
        * 정사각형으로 이루어진 섬, 바다 지도가 있을 때 섬의 갯수 카운트
        * 가로, 세로, 대각선으로 연결되어 있으면 갈 수 있다
    2. 제약사항
        * 1 <= w 너비, h 높이 <= 50
        * 둘째 줄부터 h개의 줄에 지도가 주어지고 1은 땅, 0은 바다
        * 마지막 줄에는 0이 두개 입력
2. 접근 방법
    * 모든 섬을 탐색하면서 연결된 그래프를 확인해야 한다. dfs, bfs 로 풀기
    *
"""
import sys
from collections import deque
sys.setrecursionlimit(2500)

dx = [0, 0, -1, 1, -1, 1, 1, -1]
dy = [-1, 1, 0, 0, -1, -1, 1, 1]


while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    result = 0
    grid = []
    for _ in range(h):
        grid.append(list(map(int, input().split())))

    row = len(grid)
    col = len(grid[0])
    visited = [[False] * col for _ in range(row)]


    def bfs(y, x):
        visited[y][x] = True
        queue = deque()
        queue.append((y, x))

        while queue:
            cur_y, cur_x = queue.popleft()
            for i in range(len(dx)):
                next_y = cur_y + dy[i]
                next_x = cur_x + dx[i]

                if 0 <= next_x <= col - 1 and 0 <= next_y <= row - 1 and grid[next_y][next_x] == 1:
                    if not visited[next_y][next_x]:
                        visited[next_y][next_x] = True
                        queue.append((next_y, next_x))


    def dfs(y, x):
        visited[y][x] = True

        for i in range(len(dx)):
            next_y = y + dy[i]
            next_x = x + dx[i]

            if 0 <= next_x < col and 0 <= next_y < row and grid[next_y][next_x] == 1:
                if not visited[next_y][next_x]:
                    dfs(next_y, next_x)


    for r in range(row):
        for c in range(col):
            if grid[r][c] == 1 and not visited[r][c]:
                # bfs(r, c)
                dfs(r, c)
                result += 1

    print(result)

