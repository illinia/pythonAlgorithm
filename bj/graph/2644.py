"""
1. 문제 이해
    1. 설명
        * 부모 자식간의 관계를 1촌으로 정의하여 사람들의 촌수를 계산
        * 사람들은 1 <= n <= 100 의 연속된 번호로 표시
        * 첫째 줄에 전체 사람의 수 n 주어지고, 둘째 줄에 계산해야 하는 서로 다른 두 사람의 번호가 주어진다.
        * 셋째 줄에는 부모 자식간의 관계의 개수 m 이 주어지고, 넷째 줄부터 부모 자식간의 관계를 나타내는 x, y 가 각 줄에 주어진다. 앞 번호 x 는 뒤에 나오는 정수 y의 부모번호
        * 친척 관계가 없는 경우 -1 출력
    2. 제약사항
        * 최대 노드 갯수 : 100, 최대 간선 갯수 100^2, 시간복잡도 = O(V + E) = O(100 + 100^2)
2. 접근 방법
    * 사람들을 노드로 생각하고 친척관계를 간선으로 생각, bfs 로 가장 가까운 촌수를 탐색
    * 촌수를 계산해야하므로 요구한 사람 x 부터 시작하여 탐색을 시작하고 탐색시 촌수(탐색 깊이)를 튜플에 넣어주어 탐색될때마다 1을 더해 촌수를 계산하게 한다.
    * 탐색 결과가 찾아야하는 사람인지 확인 필요
3. 코드 설계
    1. n, x, y(촌수 계산하는 대상), m 입력, graph(사전으로 정의)
    2. 전체 사람 수만큼(1 부터 n까지) graph 에 key 값으로, value 는 리스트로 저장
    3. m 만큼 반복
        1. a, b 를 입력
        2. 연결된 다른 노드를 리스트에 저장(a, b 둘다 실행)
    4. bfs 함수 정의(시작 노드 매개변수)
        1. 방문 리스트 정의(0부터 100까지 False 로 초기화), 시작 노드 위치를 방문했다고 표시(True)
        2. 큐 생성, 큐에 시작 노드 추가(노드, 촌수 = 1)
        3. 큐 빌때까지 반복
            1. 노드와 촌수를 큐에서 꺼내기
            2. graph 에서 해당 노드와 연결된 노드들 가져오기
            3. 가져온 노드들 중 원하는 노드가 있는지 확인, 있으면 해당 촌수를 반환
            4. 없으면 가져온 노드들을 반복
                1. 해당 노드가 방문된 노드인지 확인
                2. 방문하지 않았다면, 방문 처리하고, 큐에 해당 노드와 해당 촌수 + 1 추가
        4. 큐를 전부 반복했는데 원하는 노드를 찾지 못했으면 -1 반환
"""
from collections import deque
from sys import stdin

n = int(input())
x, y = map(int, input().split())
m = int(input())
graph = dict()

for i in range(1, n + 1):
    graph[i] = []

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(start, target):
    visited = [False] * 101
    visited[start] = True

    queue = deque()
    queue.append((start, 1))

    while queue:
        cur_node, cur_depth = queue.popleft()
        next_nodes_list = graph[cur_node]

        if target in next_nodes_list:
            return cur_depth

        for next_node in next_nodes_list:
            if visited[next_node] is False:
                visited[next_node] = True
                queue.append((next_node, cur_depth + 1))

    return -1


print(bfs(x, y))
