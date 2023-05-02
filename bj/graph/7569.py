"""
1. 문제 이해
    1. 설명
        * 창고에 토마토가 있고 하루가 지나면 익은 토마토 인접한 곳에 익지 않은 토마토들이 익게 된다. 저절로 익는 경우는 없다
        * 인접한 곳의 의미는 위, 아래, 왼쪽, 오른쪽 앞, 뒤 방향이다
        * M(가로칸), N(세로칸), H(높이)가 주어지고 가장 밑의 상자부터 가장 위의 상자까지 저장된 토마토의 정보가 주어진다.
        * 각 줄에는 상자 가로줄에 있는 토마토의 상태가 M 개의 정수로 주어진다.
        * 저장될 때부터 모든 토마토가 익어 있으면 0 출력, 토마토가 모두 익지 못하는 상황이면 -1 출력
        * 모든 토마토가 익게 되는 최소 일수를 구하기
    2. 제약사항
        * 일부 칸에는 토마토가 없을 수 있다.
        * 2 <= M(상자의 가로칸), N(상자의 세로칸) <= 100
        * 1 <= H(상자의 갯수) <= 100
        * 정수 1은 익은 토마토, 0은 익지 않은 토마토, -1은 없는 칸
        * 토마토는 최소 하나 이상이 있다.
2. 접근 방법
    * 가로*세로 배열을 여러개 모아놓은 3차원 배열을 사용한다. 가장 왼쪽 위, 밑의 위치는 0,0,0 이다
    * 배열 값을 입력받아 3차원 배열을 만들고 배열 요소들을 완전 탐색해서 0인 토마토가 있는지 확인하고 없으면 모든 토마토가 익은 상태이므로 0 출력
    * 이동 가능 위치 배열에 상하좌우와 위아래를 추가한다.
    * 모든 토마토가 익는 최소 일수를 구해야하므로 bfs 로 접근하되, 익은 토마토부터 탐색을 해야하는데 익은 토마토가 여러개 있을 경우 초기 큐에 모든 익은 토마토를 넣어주면 된다.
    * 큐에 위치 데이터 넣을 때 튜플로 4개의 값을 넣어준다.(x가로위치, y세로위치, z높이위치, 걸린 시간)
    * 다음 위치 이동 가능한지 확인하는 조건은 해당 x,y,z 가 0 보다 크거나 같고 M,N,H 보다 작은지 확인, 방문 리스트에서 방문했는지 확인, 다음 위치 토마토가 -1, 1이 아닌지 확인(안익은 0인 토마토만 방문)
    * 걸린 시간을 알아내기 위해 카운트를 0으로 초기화하고 다음 위치 이동 가능할 때 현재 걸린 시간 +1 과 걸린 시간 중 최댓값을 저장, 토마토 배열에서 해당 토마토값 1로 저장
    * 탐색 후 3차원 배열안에 0이 있는지 완전 탐색하여 0이 있으면 -1을 출력, 아니면 걸린 시간을 출력
3. 코드 설계
    1. M, N, H 입력
    2. 3차원 배열 tomatoes 선언, H 만큼 반복
        1. 배열 선언
        2. N 만큼 배열에 추가하고 다시 tomatoes(3차원배열) 에 추가
    3. 이동가능 위치 배열 dx, dy, dz 에 상하좌우위아래를 숫자로 표현하여 추가
    4. 방문 리스트를 3차원 배열로 같은 길이로 생성하고 False 로 초기화
    5. 덱으로 큐 생성, 걸린 시간 0으로 초기화
    6. 입력 받은 배열을 완전 탐색하여
        1. 0인 토마토가 있는지 확인하고 있으면 0 플래그 True 로 저장
        2. 1인 토마토가 발견되면 해당 위치를 큐에 추가(x, y, z, 0), 해당 위치를 방문 리스트에서 True 로 저장
    7. 순회 완료했는데도 0 플래그가 False(0인 안 익은 토마토가 없으면)이면 0 출력하고 종료
    8. 큐 빌때까지 반복
        1. 현재 x, y, z, 방문시간 저장
        2. 이동 가능한 위치 계산위해 이동 가능 배열 반복
            1. 다음 x, y, z 위치 계산
            2. 다음 이동 위치가 배열의 범위 안이고, 방문하지 않았고, 다음 위치 토마토가 -1(빈 위치), 1(이미 익은 위치, 초기 익은 토마토일 가능성도 있음) 이 아니면(0인 토마토이면)
            3. 다음 이동 위치 방문 체크하고, tomatoes 에 다음 위치 토마토값을 1로 저장하고, 걸린 시간과 현재 시간 +1 중 큰 값을 걸린 시간에 저장, 큐에 다음 x, y, z 좌표와 현재 시간 +1 하여 튜플로 큐에 저장
    9. bfs 종료 후 tomatoes 완전 탐색하여 0인 안 익은 토마토가 있는지 확인하고 있으면 -1 출력하고 종료
    10. 순회 완료하면 걸린 시간 출력
"""
import sys
from sys import stdin
from collections import deque

M, N, H = map(int, stdin.readline().split())

tomatoes = []
for _ in range(H):
    l = [list(map(str, stdin.readline().split())) for _ in range(N)]
    tomatoes.append(l)

dx = [0, 0, -1, 1, 0, 0]
dy = [-1, 1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

visited = [
    [
        [False for _ in range(M)] for _ in range(N)
    ] for _ in range(H)
]

queue = deque()
result = 0

zero_plag = False
for z in range(len(tomatoes)):
    for y in range(len(tomatoes[0])):
        for x in range(len(tomatoes[0][0])):
            tomato = tomatoes[z][y][x]
            if tomato == '0':
                zero_plag = True
            elif tomato == '1':
                queue.append((x, y, z, 0))
                visited[z][y][x] = True

if not zero_plag:
    print(0)
    sys.exit(0)

while queue:
    cur_x, cur_y, cur_z, cur_time = queue.popleft()

    for i in range(len(dx)):
        next_x = cur_x + dx[i]
        next_y = cur_y + dy[i]
        next_z = cur_z + dz[i]

        if 0 <= next_x < M and 0 <= next_y < N and 0 <= next_z < H:
            if not visited[next_z][next_y][next_x]:
                if tomatoes[next_z][next_y][next_x] == '0':
                    visited[next_z][next_y][next_x] = True
                    tomatoes[next_z][next_y][next_x] = '1'
                    next_time = cur_time + 1
                    result = max(result, next_time)
                    queue.append((next_x, next_y, next_z, next_time))

for z in range(len(tomatoes)):
    for y in range(len(tomatoes[0])):
        for x in range(len(tomatoes[0][0])):
            if tomatoes[z][y][x] == '0':
                print(-1)
                sys.exit(0)

print(result)