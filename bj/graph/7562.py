"""
1. 문제 이해
    1. 설명
        * 체스판 위에 나이트가 있을 때 몇 번 움직이면 해당 칸으로 이동할 수 있을까?
    2. 제약사항
        * 4 <= 체스판의 한 변의 길이 l <= 300
        * 체스판의 크기 = l * l
        * 체스판의 각 칸은 0 ~ l - 1, 0 ~ l - 1
2. 접근 방법
    * bfs 로 각 경우의 수를 탐색, 해당 위치가 탐색되면 그대로 반환
    * O(V + E) -> O(300^2 + 8 * 300^2) = O(90000 + 8 * 90000)
    * bfs 함수 안에 방문 2차원 배열을 선언하고 2차원 배열 요소는 False 로 초기화, 방문시 True 로 저장
    * bfs 큐에 움직인 카운트(0부터 시작)도 튜플로 저장
3. 코드 설계
    1. T(테스트 케이스 갯수) 입력, T 만큼 반복
    2. l, cur_x, cur_y, goal_x, goal_y 입력
    3. bfs 함수 정의
        1. l * l 크기의 2차원 배열을 선언하고 값들은 False 로 저장
        2. 큐 생성, 큐에 현재 x위치, y위치, 카운트 0을 튜플로 저장
        3. 큐 반복
            1. 현재 위치가 목표 위치와 같으면 현재 카운트 반환
            2. 이동 가능 위치 리스트 반복
                1. 현재 위치x, y + dx, dy 리스트 요소 더하여 다음 x, y 값 계산, 카운트 + 1하여 다음 카운트 계산
                2. 다음 x, y 위치가 가능한 위치이고, 방문하지 않은 위치이면
                    1. 방문 리스트에 위치 True 로 저장
                    2. 다음 x, y, 다음 카운트를 튜플로 큐에 저장
    4. bfs 함수 결과 출력
"""
from collections import deque
from sys import stdin

T = int(stdin.readline())
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [-1, -2, -2, -1, 1, 2, 2, 1]
for _ in range(T):
    l = int(stdin.readline())
    x, y = map(int, stdin.readline().split())
    goal_x, goal_y = map(int, stdin.readline().split())


    def bfs():
        visited = [[False] * l for _ in range(l)]
        queue = deque()
        queue.append((x, y, 0))

        while queue:
            cur_x, cur_y, cur_count = queue.popleft()

            if cur_x == goal_x and cur_y == goal_y:
                return cur_count

            for i in range(len(dx)):
                next_x, next_y = cur_x + dx[i], cur_y + dy[i]
                next_count = cur_count + 1

                if 0 <= next_x < l and 0 <= next_y < l and not visited[next_x][next_y]:
                    visited[next_x][next_y] = True
                    queue.append((next_x, next_y, next_count))


    print(bfs())

