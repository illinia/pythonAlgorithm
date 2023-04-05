"""
1. 문제 이해
    1. 설명
        * 수빈은 점 N 에 있고, 동생은 점 K 에 있다.
        * 수빈이 걸을 때 1 초 후에 x - 1, x + 1 로 이동한다. 순간이동시에는 2 * x 위치로 간다.
        * 동생을 찾을 수 있는 가장 빠른 시간 구하기
    2. 제약사항
        * 0 <= N <= 100,000
        * 0 <= K <= 100,000
2. 접근 방법
    * N 위치에서 bfs 하면서 탐색 카운트를 하고 방문 결과를 리스트에 저장하여 확인하면 될듯
    * O(V + E) -> O(100,000 + 3 * 100,000)
    * 방문 리스트에는 -1으로 초기화했다가 방문시 방문 카운트를 저장(저장된 카운트와, 새로 방문한 카운트 중 최솟값을 저장)
    * 방문 위치가 K 와 같을 때 값 저장하고 출력
3. 코드 설계
    1. N, K 저장
    2. bfs 정의
        1. 방문 리스트 N + 1 길이로 -1으로 초기화
        2. 현재 위치와 동생의 위치 (N, K) 가 같을 경우 0 반환
        3. 큐 생성, (현재 위치 N, 방문 시간 0)을 큐에 저장, 방문 리스트에 0으로 저장
        4. 큐 반복
            1. 방문 예정 위치(-1, 1, *2)를 계산하여 다음 위치 저장, 다음 방문 시간은 현재 방문 시간 + 1 로 저장
            2. 다음 위치들이 가능한 위치이고, 방문 가능하면(-1 이 아니면)
                1. 방문 리스트에 다음 방문 시간, 해당 방문 리스트 값 중 최솟값 저장
                2. 큐에 다음 위치와 다음 방문 시간을 튜플로 저장
        5. 동생의 위치를 방문 리스트에서 반환
    3. bfs 결과 출력
"""
from collections import deque

N, K = map(int, input().split())
max_index = 100000


def bfs():
    if N == K: return 0

    visited = [-1] * (max_index + 1)
    queue = deque()
    queue.append((N, 0))
    visited[N] = 0

    while queue:
        cur_location, cur_count = queue.popleft()

        next_count = cur_count + 1

        next_location_list = list()
        next_location_list.append(cur_location - 1)
        next_location_list.append(cur_location + 1)
        next_location_list.append(cur_location * 2)

        for next_location in next_location_list:
            if 0 <= next_location <= max_index and visited[next_location] == -1:
                visited[next_location] = next_count
                queue.append((next_location, next_count))

    return visited[K]


print(bfs())