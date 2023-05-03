"""
1. 문제 이해
    1. 설명
        * 적록색약은 빨간색과 초록색의 차이를 거의 느끼지 못한다.
        * N * N 인 그리드의 각 칸에 R, G, B 중 하나를 색칠한 그림이 있다.
        * 몇 개의 구역으로 나뉘어져 있는데 구역은 같은 색으로 이루어져 있다.
        * 같은 색상이 상하좌우로 인접해 있는 경우에는 두 글자는 같은 구역에 속한다.(색상의 차이를 느끼지 못하는 경우 같은 색상이라 한다.)
        * 색약이 아닌 사람이 봤을 때와 인 사람이 봤을 때 구역의 갯수를 구하라
    2. 제약사항
        * 1 <= N <= 100
2. 접근 방법
    * 그래프 탐색으로 해결할 수 있는 문제, 색약이라는 조건이 있으므로 탐색시 조건을 두가지로 하여 방문 체크와 카운트하면 될 듯
    * bfs 시 시간 복잡도는 노드 + 간선 갯수. 노드 = 10_000, 간선 갯수 = 최대 4 * 노드 갯수 = 4 * 10_000. O(5 * 10_000)이므로 초과나지 않을 것임
    * bfs 로 풀고 모든 그리드 요소들을 순회하면서 탐색
    * 탐색하면서 구역들을 나눠야한다. 최초 시작하는 요소와 같은지 확인 하는 조건으로 구역을 나눌 수 있다.
    * 방문 체크를 통해 한 구역을 전부 탐색하고 최종적으로 구역 +1을 할 수 있다.
    * 조건이 2개(색약인지 아닌지)이므로 탐색시 큐에 요소를 2개(색약구분하여) 넣고 조건 확인도 2번 하면 될듯. 방문 리스트도 해당 값을 배열로 저장하고 조건에 따라 False, True
3. 코드 설계
    1. N 입력. grid 배열 선언. N 반복하여 grid 에 배열 추가
    2. 이동 가능한 방향 x, y 배열 저장
    3. 방문 리스트를 grid 와 같은 크기로 선언하고 요소들은 [False, False] 로 초기화(색약 아닌 조건, 색약 조건)
    4. 색약 카운트, 정상 카운트 각각 0으로 초기화
    5. 각 요소들 순회(인덱스로)
        1. 최초 요소가 방문했는지 방문 리스트를 확인. 둘다 방문 했으면 다음 반복 진행
        2. 색약 여부에 따라 방문을 아직 안한(탐색 안된 구역이면) 색약, 정상 카운트 +1
        3. 큐 생성, 큐에 x, y, 방문 여부에 따라 각각 색약 여부(F, T)로 튜플로 저장하고 색약 여부에 따라 2개의 튜플을 큐에 삽입
        4. 큐 반복
            1. 현재 x, y, 색약 여부를 큐에서 뽑아서 저장
            2. 이동 가능한 방향 계산 위해 반복
                1. 다음 이동 방향 x, y, 색약 여부 저장
                2. 다음 위치가 배열 안에 위치하는지 확인, 색약 여부 따라 방문 안 했는지 확인
                3. 최초 위치 값과 다음 위동 위치 값이 일치하는지 확인, 색약 False 이면 단순히 값이 같은지만 확인
                4. 색약 True 이면 최초 위치가 R 이거나 G 일때 다음 위치가 R 이거나 G 이면 조건 통과, B 이면 B 일때만 통과
                5. 조건 일치하면 다음 위치와 색약 여부에 따라 방문 리스트에 방문 체크, 다음 x, y 위치, 색약 여부를 튜플로 큐에 저장
"""
from collections import deque
from sys import stdin

N = int(stdin.readline())
grid = [list(stdin.readline()) for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

visited = [[[False, False] for _ in range(N)] for _ in range(N)]

normal_result = 0
rg_result = 0

for i in range(N):
    for j in range(N):
        init_value = grid[i][j]
        normal_visited = visited[i][j][0]
        rg_visited = visited[i][j][1]
        if normal_visited and rg_visited:
            continue

        queue = deque()

        if not normal_visited:
            normal_result += 1
            queue.append((j, i, False))
        if not rg_visited:
            rg_result += 1
            queue.append((j, i, True))

        while queue:
            cur_x, cur_y, plag = queue.popleft()

            for d in range(4):
                next_x = cur_x + dx[d]
                next_y = cur_y + dy[d]

                if 0 <= next_x < N and 0 <= next_y < N:
                    next_value = grid[next_y][next_x]
                    # 색약이 아닌 사람
                    if not plag and not visited[next_y][next_x][0]:
                        if init_value == next_value:
                            visited[next_y][next_x][0] = True
                            queue.append((next_x, next_y, False))

                    # 색약인 사람
                    if plag and not visited[next_y][next_x][1]:
                        if ((init_value == 'R' or init_value == 'G') and (next_value == 'R' or next_value == 'G')) or init_value == next_value:
                            visited[next_y][next_x][1] = True
                            queue.append((next_x, next_y, True))

print(normal_result, rg_result)