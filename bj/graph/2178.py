"""
1. 문제 이해
    1. 설명
        * N * M 크기의 배열로 표현되는 미로가 있고 1은 이동할 수 있는 칸, 0 은 이동할 수 없는 칸
        * (1, 1) 에서 출발하여 (N, M)위치로 이동할 때 지나야하는 최소의 칸 수
        * 다른 칸 이동시 서로 인접한 칸으로만 이동할 수 있다.
    2. 제약사항
        * 2 <= N, M <= 100
2. 접근 방법
    * 그래프 탐색이고 최소 거리이니 bfs 를 이용해서 푼다.
    * O(V + E) 이므로 N*M = 10000 최대값, E = N*M * 4 최대값이므로, O(V + E) = 50000
    * 큐에 위치 넣을 때 몇 번째 탐색인지도 넣어서 카운트하여 풀기
3. 코드 설계
    1. N, M 입력
    2. graph 2차원 배열 초기화
    3. N 만큼 반복하여 입력받아서 배열에 넣기
    4. bfs 정의
        1. 방문 배열 N*M 생성
        2. 큐 생성, 첫 번째 좌표 입력(n, m, count)
        3. 큐 빌때까지 반복
        4. n, m 이 N, M 이면 카운트값 반환
        5. 아니면 이동할 수 있는지 확인하고 방문 안했으면 방문 처리, 큐 삽입(n, m, count + 1)
    5. 반환값 출력
"""
from collections import deque

N, M = map(int, input().split())

graph = [list(map(int, list(input()))) for _ in range(N)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs():
    visited = [[False] * (M + 1) for _ in range(N + 1)]
    queue = deque()
    queue.append((1, 1, 1))
    visited[1][1] = True

    while queue:
        y, x, count = queue.popleft()

        if y == N and x == M:
            return count

        for i in range(len(dy)):
            next_y = y + dy[i]
            next_x = x + dx[i]

            if 0 < next_y <= N and 0 < next_x <= M and graph[next_y - 1][next_x - 1] == 1:
                if not visited[next_y][next_x]:
                    visited[next_y][next_x] = True
                    queue.append((next_y, next_x, count + 1))


print(bfs())
