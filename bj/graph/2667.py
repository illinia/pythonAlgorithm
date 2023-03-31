"""
1. 문제 이해
    1. 설명
        * 정사각형 지도에 1은 집이 있는 곳, 0 은 집이 없는 곳
        * 연결된 곳은 상하좌우에 위치했을 때이고, 대각선은 아니다.
        * 연결된 단지 수를 출력, 오름차순으로 각 단지의 집의 수를 출력
    2. 제약사항
        * 5 <= N <= 25
2. 접근 방법
    * 그래프 탐색으로 모든 위치를 순차 반복하는데, 최초 방문시 카운트를 하면 될듯
    * 단지 별로 카운트를 해야하는데 최초 방문시 카운트 2차원 배열에 증가하는 수 1을 넣고 해당 위치에서 탐색시 모든 방문 리스트에 같은 수를 넣는다
    * 1부터 증가된 수까지 같은 수를 묶어 카운트하여 오름차순으로 출력
3. 코드 설계
    1. N 입력
    2. graph 에 입력되는 수 리스트 추가
    3. 이동 방향 리스트 초기화(상하좌우)
    4. 단지 카운트 0 초기화, 방문 2차원 배열 0으로 초기화(N*N), 단지별 카운트 딕셔너리 초기화
    5. bfs 실행
        1. 큐 생성, 첫번째 방문 요소 삽입(y, x), 해당 위치에 방문할 수 있을 시, 최초 방문시 카운트 +1
        2. 큐 빌때까지 반복
        3. 큐에서 위치 추출, 이동 방향 반복하여 다음 이동 위치 계산
        4. 해당 위치에 방문할 수 있을 시, 최초 방문시
            1. 카운트를 방문 리스트의 위치에 저장
            2. 카운트 딕셔너리에 key 없으면 생성하고, value +1
            3. 해당 위치 큐에 삽입
    6. 딕셔너리 값들 리스트로 변환하고 오름차순 정렬뒤 리스트 길이, 정렬된 리스트 출력
"""
from collections import deque

N = int(input())
graph = [list(map(int, list(input()))) for _ in range(N)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(y, x):
    queue = deque()
    queue.append((y, x))
    graph[y][x] = 0
    count = 1

    while queue:
        cur_y, cur_x = queue.popleft()

        for i in range(len(dy)):
            next_y, next_x = cur_y + dy[i], cur_x + dx[i]

            if 0 <= next_y < N and 0 <= next_x < N and graph[next_y][next_x] == 1:
                graph[next_y][next_x] = 0
                queue.append((next_y, next_x))
                count += 1
    return count


count_list = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            count_list.append(bfs(i, j))

count_list.sort()
print(len(count_list))
for i in range(len(count_list)):
    print(count_list[i])