# 4
# 7
# 1 2 4
# 1 4 6
# 2 1 3
# 2 3 7
# 3 1 5
# 3 4 4
# 4 3 2

"""
플루이드 워셜 알고리즘
* 모든 지점에서 다른 모든 지점까지 최단 경로를 모두 구해야 하는 경우에 사용할 수 있는 알고리즘
* 다익스트라 알고리즘은 단계마다 최단 거리를 가지는 노드를 하나씩 반복적으로 선택, 해당 노드를 거쳐 가는 경로를 확인하며, 최단 거리 테이블을 갱신하는 방식으로 동작
* 플로이드 워셜 알고리즘 또한 단계마다 거쳐 가는 노드를 기준으로 알고리즘을 수행, 모든 노드에 대해 다른 모든 노드로 가는 최단 거리 정보를 구한다.
* 그래서 최단 거리 정보를 2차원 리스트에 저장한다.
* 점화식은 Dab = min(Dab, Dak + Dkb)이다. 현재 확인하고 있는 노드를 제외하고 N - 1개의 노드 중에서 서로 다른 노드 (a, b)를 선택한다. n-1P2 개의 쌍을 단계마다 반복해서 확인
* 위 순열 식의 갯수는 O(N^2) 이므로 해당 반복을 N 번 반복하면 전체 시간 복잡도는 O(N^3) 이 된다.
"""

INF = int(1e9)

# 노드의 갯수 및 간선의 갯수를 입력받기
n = int(input())
m = int(input())
# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0 으로 초기화
for i in range(1, n + 1):
    graph[i][i] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
for a in range(1, n + 1):
    for b in range(1, n + 1):
        # 도달할 수 없는 경우, 무한(INFINITY)라고 출력
        if graph[a][b] == INF:
            print("INFINITY", end=" ")
        else:
            print(graph[a][b], end=" ")
    print()