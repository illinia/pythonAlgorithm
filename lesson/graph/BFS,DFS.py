"""
* 기본 bfs
* 시간 복잡도 : O(V + E) = Vertex + Edge
* 코드 설계
    1. 방문 리스트에 시작값을 넣는다
    2. 큐를 생성하고 시작값을 넣어준다.
    3. 큐가 빌때까지 반복
        1. 큐에서 선입선출하여 값을 저장한다.
        2. 해당 값을 그래프에서 찾아 연결된 노드들을 반복한다.
            1. 해당 연결된 노드가 방문되지 않았다면, 방문 리스트에 추가하고, 큐에 추가한다.
"""
from collections import deque

graph = {
	'A': ['B', 'D', 'E'],
	'B': ['A', 'C', 'D'],
	'C': ['B'],
	'D': ['A', 'B'],
	'E': ['A']
}

def bfs(graph, start_v):
    visited = [start_v]
    queue = deque()
    queue.append(start_v)

    while queue:
        cur_v = queue.popleft()
        for next_v in graph[cur_v]:
            if next_v not in visited:
                visited.append(next_v)
                queue.append(next_v)
    return visited


print(bfs(graph, 'A'))


"""
* 암시적 그래프 bfs : 2차원 배열로 그래프가 주어졌다면
1. 가로, 세로 길이가 같은 방문 리스트 생성
2. bfs 함수 정의
    1. 방향에 맞게 x, y 축 리스트 생성
    2. 최초 방문 위치 True 저장
    3. 큐 생성, 최초 위치 추가
    4. 큐가 빌때까지 반복
        1. 큐에서 x, y 축 꺼내어 저장
        2. 이동 방향들 만큼 반복
            1. 다음 x, y 위치 계산
            2. 해당 위치가 유효한지, 방문하지 않은 조건인지 확인
            3. 통과시 방문 처리, 큐에 해당 위치 추가
"""
from collections import deque

row = len(graph)
col = len(graph[0])
visited = [[False] * col for _ in range(row)]

def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited[x][y] = True
    queue = deque([(x, y)])

    while queue:
        cur_x, cur_y = queue.popleft()
        for i in range(4):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]

            if 해당 위치가 유효한 위치인지, 방문하지 않은 조건인지 확인:
                visited[next_x][next_y] = True
                queue.append((next_x, next_y))


"""
* DFS
1. 방문 리스트 생성
2. dfs 함수 생성
    1. 파라미터로 받은 현재 위치를 방문 리스트에 추가
    2. 그래프에서 현재 위치가 갈 수 있는 위치들 반복
        1. 해당 위치가 방문되지 않았으면, dfs 함수 재귀
"""