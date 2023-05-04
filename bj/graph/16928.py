"""
1. 문제 이해
    1. 설명
        * 10 * 10 크기의 100 칸으로 나누어진 보드에서 1 부터 100까지 숫자가 적혀있다.
        * 주사위를 굴려 나온 만큼 이동해야 한다. 해당 칸에는 사다리와 뱀이있어 다른 칸으로 이동한다.
        * 1번 칸에서 시작해서 100번 칸으로 이동하는 것이 목표이고, 100 번칸을 넘어가면 이동할 수 없다.
        * 주사위를 굴리는 최솟값을 구하기
    2. 제약사항
        * 1 <= N 사다리 수 <= 15
        * 1 <= M 뱀의 수 <= 15
        * 1, 100번 칸은 뱀과 사다리의 시작 또는 끝이다. 모든 칸은 최대 하나의 사다리, 뱀을 가지고 있고 동시에 가지진 못한다.
2. 접근 방법
    * 칸들을 이동할 수 있는 간선들이 있고 최솟값을 구하는 문제이므로 bfs 를 사용한다.
    * 노드의 갯수는 100, 간선의 갯수는 최대 100 * 6 * 2. 시간초과 나지 않음
    * 방문 리스트는 칸이 100개로 정해져있으므로 101개의 배열을 만들고 False 로 초기화
    * 1번 부터 시작하여 주사위를 굴려 1 ~ 6까지 수를 더한 다음 칸을 계산하여 이동하고 조건이 충족되면 이동한 칸에 방문 처리를 한다.
    * 이동시 칸이 보드 안에서 유효한지 확인(100번 이하인 경우가 조건), 방문하지 않았으면 조건 통과
    * 이동한 칸이 사다리나 뱀이 있는지 확인하고 사다리나 뱀이 없으면 방문 체크하고 이동한 칸을 큐에 넣을 때 굴린 횟수 +1을 해준다.
    * 사다리나 뱀이 있으면 사다리와 뱀을 타고 다음 칸으로 이동한다. 조건 확인하고 통과시 이동한 칸에 방문 처리를 하고 큐에 넣을 때 굴린 횟수 +1을 한다.
    * 한 칸에 사다리나 뱀이 최대 1개 있으므로 이동 후 다시 체크할 필요는 없다.
    * 이렇게 이동하면서 100 번째 칸이 나오면 굴린 횟수 +1을 출력하고 반복 종료
3. 코드 설계
    1. 방문 리스트 False * 101 로 초기화
    2. N, M 입력, N + M 번 반복하면서 사다리와 뱀의 시작, 끝 위치를 dict 로 key, value 매핑
    3. 큐 선언, 큐에 1(첫번째 칸 위치), 0(주사위 굴린 횟수) 튜플로 저장, 방문 확인
    4. 큐 반복
        1. 현재 위치, 현재 횟수를 큐에서 뽑아서 저장
        2. 주사위를 1 ~ 6까지 굴려서 확인하기 위해 반복
            1. 다음 위치 계산하여 변수 저장하고, 현재 위치가 100 인지 확인. 100이면 현재 횟수 +1 출력하고 반복 종료
            2. 100이 아니면 해당 위치가 100 미만인지 확인, 방문하지 않았는지 확인
            3. 조건 통과시 이동한 칸 방문 체크하고, 이동한 칸에 해당하는 key 가 dict 에 존재하는지 확인
                1. key 가 존재한다면 다음 칸으로 이동해야 하므로 다음 위치를 value 값으로 저장
                2. 이동한 칸의 조건(방문하지 않았는지) 확인하고 통과시 이동한 칸의 방문 체크하고 큐에 이동한 칸 위치, 굴린 횟수 +1하여 저장
                3. key 가 존재하지 않는다면 사다리나 뱀이 없으므로 큐에 이동한 칸, 굴린 횟수 +1을 추가한다.
"""
from collections import deque
import sys

visited = [False] * 101

N, M = map(int, input().split())
move = dict()

for _ in range(N + M):
    a, b = map(str, input().split())
    move[a] = b

queue = deque()
queue.append((1, 0))
visited[1] = True

while queue:
    cur_location, cur_count = queue.popleft()

    for i in range(1, 7):
        next_location = cur_location + i

        if next_location == 100:
            print(cur_count + 1)
            sys.exit(0)

        if next_location < 100 and not visited[next_location]:
            visited[next_location] = True

            if str(next_location) in move:
                next_location = int(move[str(next_location)])

                if not visited[next_location]:
                    visited[next_location] = True
                    queue.append((next_location, cur_count + 1))
            else:
                queue.append((next_location, cur_count + 1))