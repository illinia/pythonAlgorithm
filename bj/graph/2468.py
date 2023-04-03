"""
1. 문제 이해
    1. 설명
        * 행과 열의 길이가 N 인 2차원 배열이 주어졌을 때 배열의 각 원소는 해당 지점의 높이를 표시하는 자연수
        * 특정 높이 만큼 비가내려 높이 이하의 지점이 물에 잠겼다고 하면 잠기지 않는 영역들의 갯수를 구하기
    2. 제약사항
        * 2 <= N <= 100
        * 1 <= 높이 <= 100
2. 접근 방법
    * 비가 오는 높이 만큼 모든 배열의 값들에서 빼고 1 이상인 분리된 섬의 갯수를 구하면 됨
    * 그래프 탐색으로 풀고, O(V + E) 이므로 O(10^4 + 10^4 * 4) 이고 장마철 비의 높이가 100 개이므로 10^2 곱하면 O(10^6)
    * 비 높이는 1 부터 100까지라 가정
3. 코드 설계
    1. N 입력, 빈 배열 리스트 초기화 graph
    2. graph 에 N 만큼 반복하여 높이 리스트 저장, 섬 최댓값 0 초기화
    3. 이동 가능한 방향 리스트 dy, dx 상하좌우 초기화
    4. 비 계산 함수 정의(비 높이)
        1. 방문리스트 N*N False 로 초기화, 카운트 0 초기화
        2. 0 ~ N - 1만큼 두번 반복하여 i, j 값을 bfs 함수에 전달
        3. bfs 함수 반환값을 카운트에 더하기
        4. 카운트 반환
    5. bfs 함수 정의(복사하고 비 높이 만큼 차감해준 graph 입력, 방문리스트, 방문 y, x 좌표)
        0. y, x 위치를 방문했거나, 1 보다 작으면, 0 반환
        1. 큐 생성, 시작 위치 (y, x) 큐에 저장
        2. 큐 반복
        3. 상하좌우 이동 위치 반복
            1. 해당 위치가 배열에서 가능한 위치인지, 위치의 값이 1 이상인지, 방문하지 않았는지
            2. 조건 통과시 방문 리스트에 방문 표시, 해당 위치를 큐에 저장
        4. 큐 반복 종료 후 1 반환
    6. 비 높이(1 ~ 배열 최댓값) 반복하여 비 계산 함수에 전달
    7. 비 계산 함수 반환값과 섬 최댓값 중 큰 값을 섬 최댓값에 저장
    8. 섬 최댓값 출력
"""
import copy
from collections import deque

N = int(input())
origin_graph = []

for _ in range(N):
    origin_graph.append(list(map(int, input().split())))

max_result = 0

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def rain_cal(rain_height):
    visited = [[False] * N for _ in range(N)]
    count = 0

    cal_graph = copy.deepcopy(origin_graph)

    for i in range(len(cal_graph)):
        for j in range(len(cal_graph[i])):
            cal_graph[i][j] -= rain_height

    for i in range(N):
        for j in range(N):
            count += bfs(cal_graph, visited, i, j)

    return count


def bfs(graph, visited_list, y, x):
    if visited_list[y][x] or graph[y][x] < 1:
        return 0

    queue = deque()
    queue.append((y, x))

    while queue:
        cur_y, cur_x = queue.popleft()
        for i in range(len(dy)):
            next_y = dy[i] + cur_y
            next_x = dx[i] + cur_x

            if 0 <= next_y < N and 0 <= next_x < N and graph[next_y][next_x] >= 1 and not visited_list[next_y][next_x]:
                visited_list[next_y][next_x] = True
                queue.append((next_y, next_x))

    return 1


max_height = max(map(max, origin_graph))
for i in range(0, max_height + 1):
    max_result = max(rain_cal(i), max_result)

print(max_result)