"""
1. 문제 이해
    1. 설명
        * N * M 종이 위에 테트로미노를 놓으려하고 각 종이 칸에는 숫자가 적혀있다.
        * 테트로미노가 놓인 칸에 있는 숫자 합의 최대값을 구하기
    2. 제약사항
        * 4 <= N, M <= 500
2. 접근 방법
    * 처음엔 완전탐색으로 테트로미노 경우들을 전부 계산하려 했으나 다른 방법 생각
    * dfs 로 풀면 노드 = 25_000, 간선 = 4 * 25_000. 시간초과 안남
    * ㅗ 모양의 도형 외에는 특정 점으로 부터 4번 탐색했을 때 나오는 도형들이므로 dfs 로 해결할 수 있다.
    * ㅗ 모양의 경우 두번째 방문한 위치에서 다음 방문 처리하고 해당 수를 더하고 다시 dfs 탐색시 다음 위치가 아니라 현재 위치에서 탐색하면 ㅗ 모양을 만들 수 있다.
    * 이동 가능한 위치는 배열로 선언(상하좌우)
    * dfs 함수에 필요한 매개변수는 x, y 위치, 합한 수, 탐색 깊이. 탐색 깊이는 처음 1으로 시작
    * 전체 탐색의 최댓값을 구해야하므로 최상단에 최댓값 변수를 저장(0), 종료 조건으로는 탐색을 4번하였을 때 최댓값과 비교하고 저장한 후 dfs 종료
    * 방문 조건은 x, y 위치가 배열안에 있는지, 방문하지 않았는지
    * 각 dfs 함수를 실행할때 최댓값과 비교한 경우 마지막으로 방문한 곳부터 방문 체크를 해제해야 다음 dfs 탐색시 탐색할 수 있음
3. 코드 설계
    1. N, M 입력, grid 선언, N 번 반복하여 grid 에 배열들 입력
    2. 출력 최댓값 0 으로 초기화
    3. 방문 리스트를 grid 와 동일한 크기로 선언, False 로 초기화, 이동 가능한 위치 배열 초기화
    4. dfs 함수 정의(x, y, 합한 수, 탐색 깊이)
        1. depth 가 4인 경우(4번 탐색한 경우) 출력 최댓값과 현재 더한 값을 비교하여 최댓값을 저장
        2. 현재 위치부터 상하좌우를 탐색하기 위해 반복
            1. 다음 위치 저장
            2. 다음 위치가 조건에 맞는지 확인하고 조건 통과시
                1. 통과한 위치를 방문 체크하고
                2. dfs 함수에 다음 위치 x, y, 합한 수 파라미터 + 현재 위치 값, 파라미터 depth + 1 을 넣어 실행
                3. dfs 함수 종료시 현재 통과한 위치를 방문 체크 해제
                4. ㅗ 모양을 탐색하기 위해 depth 파라미터가 2인지 확인
                    1. 맞으면 다음 위치 방문 체크
                    2. dfs 탐색시 다음 x, y 위치를 현재 위치, 합한 수 파라미터 + 현재 위치 값, 파라미터 depth + 1 을 넣어 실행
                    3. dfs 탐색 종료 후 다음 위치 방문 체크 해제
    5. grid 모든 요소 순회
        1. 탐색 초기 위치 방문 체크
        2. dfs 에 초기 위치, 현재 위치 값, depth 1 넣어 실행
        3. 탐색 종료 후 방문 체크 해제
    6. 최댓값 출력
"""
from sys import stdin

N, M = map(int, stdin.readline().split())
grid = [list(map(int, stdin.readline().split())) for _ in range(N)]

max_value = max(map(max, grid))
result = 0

visited = [[False] * M for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def dfs(x, y, sum_value, depth):
    global result

    if result >= sum_value + max_value * (4 - depth):
        return

    if depth == 4:
        result = max(result, sum_value)
        return

    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]

        if 0 <= next_x < M and 0 <= next_y < N and not visited[next_y][next_x]:
            visited[next_y][next_x] = True
            dfs(next_x, next_y, sum_value + grid[next_y][next_x], depth + 1)
            visited[next_y][next_x] = False

            if depth == 2:
                visited[next_y][next_x] = True
                dfs(x, y, sum_value + grid[next_y][next_x], depth + 1)
                visited[next_y][next_x] = False


for y in range(N):
    for x in range(M):
        visited[y][x] = True
        dfs(x, y, grid[y][x], 1)
        visited[y][x] = False

print(result)
