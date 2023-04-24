"""
1. 문제 이해
    1. 설명
        * 5x5 크기의 숫자판이 있고 각 칸에 숫자(0 ~ 9)가 적혀있다.
        * 임의의 위치에서 시작해서 인접해있는 네 방향으로 다섯 번 이동하면서, 각 칸에 적혀있는 숫자를 차례로 붙이면 6자리 수가 된다.
        * 이동할 때는 한 번 거쳤던 칸을 다시 거쳐도 되고, 0으로 시작하는 수도 만들 수 있다.
2. 접근 방법
    * 5*5 크기의 숫자판이므로 완전 탐색을 해도 25 * 4 * 6이므로 시간초과나지 않을 듯
    * 최종적으로 만들어진 숫자를 저장하여 중복을 없애고 길이 출력하면 될듯
    * dfs 로 풀기
3. 코드 설계
    1. 숫자판 리스트 생성
    2. 5 번 만큼 숫자 리스트를 입력받아서 숫자판에 저장
    3. 결과 집합을 생성
    4. 이동 가능한 범위를 나타내는 dx, dy 리스트(상하좌우)를 초기화
    5. dfs 함수 정의(y, x 좌표 파라미터, 만들어진 숫자열)
        1. 이동 가능한 범위 4개를 반복
            1. 이동할 위치가 가능한지(숫자판 범위 안) 확인하고
            2. 가능하고 파라미터 숫자열 길이가 5이면(탐색 종료) 파라미터 숫자열 + 해당 숫자 결과를 결과 집합에 추가
            3. 파라미터 숫자열 길이가 5보다 작으면(계속 탐색) dfs 재귀 호출(이동한 위치 y, x 좌표, 파라미터 숫자열 + 이동한 위치 숫자)
    6. 숫자판 모든 위치에서 dfs 실행
    7. 결과 집합 길이 출력
"""
board = []
for _ in range(5):
    board.append(list(map(str, input().split())))

result = set()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def dfs(y, x, number_str):
    for i in range(len(dx)):
        next_y = y + dy[i]
        next_x = x + dx[i]

        if 0 <= next_y < 5 and 0 <= next_x < 5:
            next_number_str = number_str + board[next_y][next_x]
            if len(number_str) == 5:
                result.add(next_number_str)
            else:
                dfs(next_y, next_x, next_number_str)


for y in range(len(board)):
    for x in range(len(board[0])):
        dfs(y, x, board[y][x])

print(len(result))