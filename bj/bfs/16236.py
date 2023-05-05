"""
1. 문제 이해
    1. 설명
        * N*N 공간에 물고기 M 마리와 아기상어 1마리가 있다. 공간은 1*1 정사각형 칸으로 되어있고 한 칸에는 물고기가 최대 1마리 존재한다.
        * 아기 상어와 물고기는 모두 크기를 가지고 있다. 처음 아기 상어 크기는 2이고, 1초에 상하좌우로 인접한 한 칸씩 이동한다.
        * 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없고, 나머지 칸은 모두 지나갈 수 있다.
        * 자신의 크기보다 작은 물고기만 먹을 수 있다. 크기가 같은 물고기는 먹을 수 없지만 지나갈 수 있다.
        * 어디로 이동할 지 결정하는 방법
            * 더 이상 먹을 수 있는 물고기가 없으면 도움 요청한다.
            * 먹을 수 있는 물고기가 1마리면 그 물고기를 먹으러 간다.
            * 1마리보다 많으면, 거리가 가장 가까운 물고기를 먹으러 간다.
                * 거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 갯수의 최솟값이다.
                * 거리가 가까운 물고기가 많다면 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
        * 이동은 1초가 걸리고 먹는데 걸리는 시간은 없다. 먹을 수 있는 물고기가 있는 칸으로 이동했으면 이동과 동시에 물고기를 먹는다. 먹으면 빈 칸이 된다.
        * 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가한다.
        * 몇 초 동안 엄마 상어에게 도움을 요청하지 않고 물고기를 먹을 수 있는지 구하기
    2. 제약 사항
        * 2 <= N <= 20
        * 0 : 빈 칸, 1 ~ 6 : 칸에 있는 물고기의 크기, 9 : 아기 상어 위치
2. 접근 방법
    * 이동시 항상 물고기의 위치들을 계산하여 순서대로 이동해야 하므로 bfs 를 사용한다.
    * 이동 위해서 계산할 때 필요한 정보들은 아기 상어의 크기, 먹을 수 있는 물고기들의 위치, 어떤 물고기를 먼저 먹을지 우선순위를 정해주는 함수
    * 아기 상어의 크기는 최상위 스코프에서 변수로 저장, 먹은 물고기의 갯수도 변수로 저장. 먹을 때 마다 먹은 갯수를 카운트하여 크기와 비교하여 크기를 증가, 카운트를 0으로 초기화
    * 공간(grid)을 순회하여 물고기의 크기를 확인하여 먹을 수 있는 물고기의 위치(현재 위치 기준으로 위쪽 우선, 그 다음 왼쪽 우선) 리스트를 반환해주는 함수를 구현
        * 해당 함수를 실행할 때 이동 가능한 물고기들만 탐색하여 거리를 계산한다. 따라서 다른 함수에서 bfs 돌면서 조건 탐색할 필요가 없음
        * 해당 함수 내에서 방문 확인 리스트 필요
        * 반환할 리스트에는 x, y, 거리 3개를 튜플로 추가
        * bfs 조건은 다음 위치가 배열 안에 있는지, 방문하지 않았는지, 해당 위치가 아기 상어 크기보다 같거나 작은지
        * 모든 조건 통과하고 물고기가 있고(0이 아니고) 물고기 크기가 아기 상어 크기보다 작으면 물고기 x, y 위치, 상어 위치로 부터의 거리를 저장, 먹을 수 없는 물고기면 큐에 다음 위치, 현재 거리 +1 을 튜플로 추가
        * 리턴 리스트를 정렬해줄 때 오름차순으로 거리, y, x 순으로 정렬한다. 그리고 리턴한다.
    * 먹을 수 있는 물고기 리스트를 받아서 리스트의 길이가 0 이면 먹을 수 있는게 없으므로 현재 걸린 시간 출력하고 종료
    * 먹을 수 있는 물고기 자리에 상어 위치 저장, 기존 상어 위치는 0으로 저장, 물고기와의 거리 만큼 소요 시간에 더하기, 먹은 갯수 카운트 +1, 아기 상어 크기와 먹은 갯수 카운트가 같다면 크기 +1, 먹은 카운트 0 저장
3. 코드 설계
    1. N 입력, grid 배열 선언, N 만큼 반복하며 grid 에 배열들 입력
    2. 아기 상어 크기(weight) 를 2로 초기화, 먹은 갯수 카운트(count) 를 0으로 초기화, 이동한 전체 시간(move_time) 0으로 초기화
    3. 이동 방향 리스트(상하좌우) 저장, 현재 상어 위치 x, y를 변수로 저장, 배열 탐색하면서 상어 발견시 현재 상어 위치에 저장
    4. 먹을 수 있는 물고기들 리스트를 반환하는 함수 정의(현재 위치 x, y) (search_fish)
        1. 방문 확인 리스트를 grid 와 같은 크기로 False 로 초기화
        2. 반환할 리스트 선언, 현재 상어 위치 방문 체크
        3. 큐 선언, 큐에 현재 상어 위치 x, y, 거리 = 0 을 튜플로 추가
        4. 큐 반복
            1. 다음 위치 x, y 저장 위해 반복, 위치 저장
            2. 다음 위치가 배열안에 존재하는지, 방문하지 않았는지, 다음 위치의 값이 아기 상어 크기보다 같거나 작은지(0~아기 상어 크기)
                1. 조건 통과시 다음 위치 값이 0 초과 아기 상어 크기 미만이면 물고기 x, y 위치, 상어 위치로부터 거리(현재 거리 + 1)를 리턴 리스트에 저장
                2. 먹을 수 없는 물고기이면 다음 탐색을 위해 다음 x, y 위치, 현재 거리 +1 을 튜플로 큐에 추가
        5. 큐 반복이 종료되면 반환할 리스트를 정렬(오름차순으로 거리, y, x 순으로 정렬)
        6. 리스트 반환
    5. 무한 반복
        1. search_fish 함수로 현재 상어 위치를 넣어 먹을 수 있는 물고기 리스트를 반환
        2. 해당 리스트가 빈 리스트이면 move_time 을 출력하고 종료
        3. 빈 리스트가 이나면 첫 번째 요소(물고기 위치, 거리)를 저장하고 move_time 에 거리를 더하고, count 에 +1, 물고기 위치에 9를 저장, 상어 위치에 0 저장, 물고기 x, y 값을 현재 상어 위치에 저장
        4. weight 가 count 와 같다면 weight +1, count = 0
"""
import sys
from sys import stdin
from collections import deque

N = int(input())
grid = [list(map(int, stdin.readline().split())) for _ in range(N)]

weight = 2
count = 0
move_time = 0

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

shark_x = 0
shark_y = 0

for i in range(N):
    for j in range(N):
        if grid[i][j] == 9:
            shark_y = i
            shark_x = j
            break


def search_fish(x, y):
    visited = [[False] * N for _ in range(N)]
    visited[y][x] = True
    return_list = []

    queue = deque()
    queue.append((x, y, 0))

    while queue:
        cur_x, cur_y, cur_distance = queue.popleft()

        for i in range(4):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]

            if 0 <= next_x < N and 0 <= next_y < N and not visited[next_y][next_x] and grid[next_y][next_x] <= weight:
                visited[next_y][next_x] = True
                if 0 < grid[next_y][next_x] < weight:
                    return_list.append((next_x, next_y, cur_distance + 1))
                else:
                    queue.append((next_x, next_y, cur_distance + 1))

    return_list.sort(key=lambda l: (l[2], l[1], l[0]))
    return return_list


while True:
    fish_list = search_fish(shark_x, shark_y)

    if len(fish_list) == 0:
        print(move_time)
        sys.exit(0)

    fish_x, fish_y, fish_distance = fish_list[0]
    move_time += fish_distance
    count += 1
    grid[fish_y][fish_x] = 9
    grid[shark_y][shark_x] = 0
    shark_x, shark_y = fish_x, fish_y

    if weight == count:
        weight += 1
        count = 0

