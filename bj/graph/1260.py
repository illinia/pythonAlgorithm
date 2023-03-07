"""
1. 문제 이해
    1. 설명
        * dfs, bfs 로 탐색한 결과를 출력하는 프로그램 작성
        * 방문할 수 있는 정점이 여러 개인 경우 정점 번호가 적은 것을 먼저 방문
        * 더 이상 방문할 수 없는 경우 종료
    2. 제약사항
        * 1 <= 정점의 갯수 N <= 1,000
        * 1 <= 간선의 갯수 M <= 10,000
        * 탐색을 시작할 정점의 번호 V
        * M 개의 줄에 간선이 연결하는 두 정점의 번호가 주어지고 양방향이다.
        * 출력의 첫 줄에 dfs, 둘째 줄에 bfs
2. 접근 방법
    * O(V + E) 이므로 O(11,000) 이다
    * 양방향 그래프이므로 서로 추가해줘야 한다.
    * 단순히 노드 탐색만 하는 직관적인 그래프이므로 해시 테이블에 리스트로 저장
    * 정점 번호가 적은 것을 먼저 방문하기 위해서는 간선 리스트를 정렬해야한다. 정렬시 O(ElogE)
3. 코드 설계
    1. N, M, V 입력, 그래프 딕셔너리 생성
    2. M 만큼 반복하여 간선 입력(두 정점에 모두 입력해야함)
    3. bfs, dfs 결과 리스트 생성, bfs, dfs 방문 처리 위한 딕셔너리 생성
    4. bfs 함수 생성
        1. 큐 생성, 최초 정점 입력
        2. 큐가 빌때까지 반복
            1. 해당 정점이 방문할 수 있는 정점들 리스트 반복
                1. 반복시 방문했는지 확인, 방문 안했으면 방문 처리
                2. 해당 정점 방문 결과 리스트에 추가
                3. 해당 정점을 큐에 삽입
    5. dfs 함수 생성
        1. 해당 정점이 방문할 수 있는 리스트 반복
            1. 방문 했는지 확인, 방문 안했으면 방문 처리
            2. 해당 정점 방문 결과 리스트에 추가
            3. 해당 정점을 dfs 함수 실행
    6. 결과 리스트 출력
"""
from collections import deque
from sys import stdin

N, M, V = list(map(int, stdin.readline().split()))
graph = dict()

for _ in range(M):
    a, b = list(map(int, stdin.readline().split()))
    if a in graph:
        graph[a].append(b)
    else:
        graph[a] = [b]

    if b in graph:
        graph[b].append(a)
    else:
        graph[b] = [a]

for g in graph.values():
    g.sort()

bfs_result = []
dfs_result = []
bfs_visit = {}
dfs_visit = {}


def bfs(init_v):
    queue = deque()
    queue.append(init_v)
    bfs_visit[init_v] = True
    bfs_result.append(str(init_v))

    while queue:
        popleft = queue.popleft()

        if popleft not in graph:
            return
        cur_list = graph[popleft]
        for cur_v in cur_list:
            if cur_v not in bfs_visit:
                bfs_visit[cur_v] = True
                bfs_result.append(str(cur_v))
                queue.append(cur_v)


def dfs(init_v):
    dfs_visit[init_v] = True
    dfs_result.append(str(init_v))
    if init_v not in graph:
        return
    cur_list = graph[init_v]

    for cur_v in cur_list:
        if cur_v not in dfs_visit:
            dfs(cur_v)


bfs(V)
dfs(V)

print(' '.join(dfs_result))
print(' '.join(bfs_result))











