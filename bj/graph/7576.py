"""
1. 문제 이해
    1. 설명
        * 토마토가 격자 모양의 상제 칸에 하나씩 보관된다. 익은것, 안익은 것이 있고 하루가 지나면 익은 토마트에 인접해있는 안익은 토마토들이 익게 된다.(상하좌우)
        * 토마토가 다 익게 되는 최소 일수를 구하라. 일부 칸에는 토마토가 없을 수 있다.
    2. 제약사항
        * 상자 가로 M, 세로 N 이 있고 2 <= M, N <= 1,000
        * 1은 익은 토마토, 0은 익지 않은 토마토, -1은 토마토가 없는 칸
        * 처음부터 모든 토마토가 익었으면 0 출력, 모두 익지 못하면 -1 출력, 모두 익을 수 있다면 최소 날
# 2. 접근 방법
#     * 격자 모양의 그래프에서 탐색을 하면서 값을 변경하고 최소 시간을 구하는 문제이므로 bfs 로 푼다.
#     * 저장될 때부터 모든 토마토가 익어있는 상황이면 0을 출력, 모든 칸 bfs 한 후 안 익은 토마토가 있으면 -1 출력
#     * 모든 칸에서 bfs 를 하여 최소 날을 구하여 저장
#     * 탐색을 시작한 칸이 익어있지 않은 상태인지 확인하고 익어있지 않으면 리턴, 익어있으면 탐색 시작
#     * 상하좌우 칸을 탐색하는데 배열의 범위를 벗어나지 않았는지 확인
#     * 해당 칸의 값이 -1(토마토가 없는칸)이 아닌지 확인
#     # * 1(익은 토마토)이면 방문 체크 필요없이 큐 넣고(최솟값을 구하므로 +1하는 것은 상관없음)
#     # * 0(안 익은 토마토)이면 방문 체크하고 큐 넣기
#     * 방문 리스트에 방문 횟수를 저장하는 식으로 방문했는지 확인하기 위해서 초기값 0 으로 저장, 방문하면 이전 방문값 + 1하여 저장
# 3. 코드 설계
#     1. M(가로), N(세로) 입력
#     2. 배열(토마토 칸)에 N 만큼 반복하여 배열 입력하여 2차원 배열로 저장계
#     3. 이동 가능한 위치 dr, dc 정의(상하좌우)
#     4. 방문 최솟값을 -1로 저장
#     5. bfs 함수 정의(row, col)
#         1. 방문 리스트를 토마토 칸 배열과 같은 크기로 정의하고 0 으로 초기화
#         2. 큐 생성, 큐에 row, col 값 튜플로 넣기, 리턴할 최댓값을 0으로 초기화
#         3. 큐 반복
#             1. 현재 row, col 큐에서 뽑아서 저장
#             2. 이동 가능한 위치를 얻기 위해 반복
#                 1. 다음 이동할 위치가 배열안에 있는지,
#                 2. 다음 이동할 위치 값이 -1이면 방문 리스트에도 -1 로 저장하고 해당 반복문 건너뜀
#                 3. 다음 이동할 위치 값이 0 이면 방문 리스트에 현재 방문 리스트 값 + 1하여 다음 방문 리스트 값에 저장
#                 4. 큐에 다음 이동할 위치를 튜플로 저장
#         4. 큐 반복 끝나고 방문 리스트 모든 원소를 탐색하여 0(익지 않은 토마토)가 있으면 해당 함수는 -1(토마토가 익지 못하는 상황) 리턴
#         5. 모든 원소 탐색시 0보다 크면(0, -1 이 아니면) 해당 값과 최댓값 비교하여 최댓값에 저장
#         5. 방문 리스트에서 최댓값을 리턴
#     6. bfs 리턴값을 방문 최솟값에 저장시 방문 최솟값이 -1 이 아닌지 확인하고 저장할 값이 -1보다 큰지 확인하고 저장
2. 접근 방법
    * 배열 입력 후 0이 없는지 확인하고 하나라도 1 이 있으면 모든 토마토가 이미 익은 상태이므로 0 반환, 아니면 계속 진행
    * 하나의 칸을 선택해서 탐색하는게 아니라 토마토가 익은 모든 칸을 선택해서 탐색해야함
    * 방문 카운트 배열로 카운트했지만 복잡해지므로 큐에 위치 넣을 때 카운트도 같이 넣어주기
    * 방문 조건은 다음 위치가 배열 범위에서 벗어나지 않는지, 다음 값이 -1, 1(익은 토마토이면 이미 탐색중이므로) 이 아닌지
    * 큐 반복 바깥의 스코프에 카운트 변수를 선언해놓고 다음 방문 위치 방문이 확정되면 다음 카운트와 현재 카운트 변수를 비교해서 큰 값을 저장
    * 큐 반복 종료 후 모든 배열값을 순회하며 0인 값이 있는지 확인, 있으면 -1 반환
3. 코드 설계
    1. M(가로), N(세로) 입력
    2. 배열(토마토 칸)에 N 만큼 반복하여 배열 입력하여 2차원 배열로 저장계
    3. 큐 선언
    4. 배열 모든 요소 순회
        1. 0있으면 플래그 True
        2. 1있으면 플래그 True, 큐에 해당 좌표, 0 총 3개를 튜플에 저장하여 큐에 추가
    5. 0이 없는지 확인, 1이 하나라도 있으면 모든 토마토가 이미 익은 상태이므로 0 반환하고 종료, 아니면 계속 진행
    6. 이동 가능한 위치 dx, dy (상하좌우) 배열로 선언
    7. 전체 방문 카운트 0으로 초기화, 방문 2차원 배열 False 로 초기화
    8. 큐 반복
        1. 현재 x, y 위치, 방문 카운트 큐에서 뽑아서 저장
        2. 이동 가능한 위치 배열 반복
            1. 다음 이동할 위치 저장
            2. 다음 이동할 위치가 배열안에 있는지, 방문을 아직 안했는지, 값이 0인지
            3. 조건 통과하면 다음 방문 카운트를 현재 방문 카운트 +1 하고 전체 방문 카운트와 비교해서 최댓값을 저장 토마토 값을 1로 저장(익은)
            4. 큐에 다음 방문 x, y 위치, 다음 방문 카운트 저장
    9. 큐 반복 끝나고 방문 리스트 모든 원소를 탐색하여 0(익지 않은 토마토)가 있으면 해당 함수는 -1(토마토가 익지 못하는 상황) 리턴
    10. 없으면 전체 방문 카운트를 출력

"""
import sys
from sys import stdin
from collections import deque

M, N = map(int, input().split())
data = [list(map(int, stdin.readline().split())) for _ in range(N)]
queue = deque()

exist_zero = False
exist_one = False

for i in range(N):
    for j in range(M):
        tomato = data[i][j]
        if tomato == 0:
            exist_zero = True
        elif tomato == 1:
            exist_one = True
            queue.append((i, j, 0))

if not exist_zero and exist_one:
    print(0)
    sys.exit(0)

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

total_visit_count = 0
visit = [[False] * M for _ in range(N)]

while queue:
    cur_y, cur_x, cur_visit_count = queue.popleft()

    for i in range(len(dy)):
        next_y = cur_y + dy[i]
        next_x = cur_x + dx[i]

        if 0 <= next_y < N and 0 <= next_x < M and not visit[next_y][next_x] and data[next_y][next_x] == 0:
            next_visit_count = cur_visit_count + 1
            total_visit_count = max(total_visit_count, next_visit_count)
            data[next_y][next_x] = 1
            queue.append((next_y, next_x, next_visit_count))

for i in range(N):
    for j in range(M):
        if data[i][j] == 0:
            print(-1)
            sys.exit(0)

print(total_visit_count)



# from sys import stdin
# from collections import deque
#
# M, N = map(int, input().split())
# data = [list(map(int, stdin.readline().split())) for _ in range(N)]
#
# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]
#
# min_visit = 987654321
#
#
# def bfs(row, col):
#     visit_count = [[0] * M for _ in range(N)]
#     visited = [[False] * M for _ in range(N)]
#     visited[row][col] = True
#
#     queue = deque()
#     queue.append((row, col))
#     max_value = 0
#
#     while queue:
#         cur_row, cur_col = queue.popleft()
#
#         for i in range(len(dc)):
#             next_row = cur_row + dr[i]
#             next_col = cur_col + dc[i]
#
#             if 0 <= next_row < N and 0 <= next_col < M and not visited[next_row][next_col]:
#                 next_value = data[next_row][next_col]
#                 if next_value == -1:
#                     visit_count[next_row][next_col] = 1
#                     visited[next_row][next_col] = True
#                     continue
#
#                 if next_value == 0:
#                     visited[next_row][next_col] = True
#                     visit_count[next_row][next_col] = visit_count[cur_row][cur_col] + 1
#                     queue.append((next_row, next_col))
#
#     for i in range(N):
#         for j in range(M):
#             if visit_count[i][j] == 0 and data[i][j] != 1:
#                 return -1
#             elif visit_count[i][j] > 0:
#                 max_value = max(max_value, visit_count[i][j])
#
#     return max_value
#
#
# for i in range(N):
#     for j in range(M):
#         if data[i][j] == 1:
#             result = bfs(i, j)
#             print(result)
#             min_visit = min(min_visit, result)
#
# print(min_visit)
