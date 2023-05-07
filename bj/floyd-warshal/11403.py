"""
1. 문제 이해
    1. 설명
        * 가중치 없는 방향 그래프 G 가 주어졌을 때 모든 정점(i, j) 에 대해 i 에서 j 로 가는 경로가 있는지 없는지 구하기
        * 정점의 갯수 N입력, N 개 만큼 그래프의 인접 행렬 주어짐.
    2. 제약사항
        * 1 <= N <= 100
2. 접근 방법
    * 모든 위치에 대해 다른 모든 위치로 이동 가능한지 확인해야 함. 플루이드 워셜을 사용
    * 그래프를 그대로 사용하여 연결 가능한 곳을 수정
    * 3중 반복문을 사용하는데 연결하는 기준은 a -> k, k -> b 가 전부 1이면 연결되었다는 뜻이므로 (a, b) 를 결과 리스트에 1로 저장
3. 코드 설계
    1. N 입력, G 선언
    2. N 만큼 반복하여 배열을 G 에 저장
    3. 0 부터 N - 1까지 3중 반복(k, a, b)
        1. a -> k, k -> b가 1이라면(연결되어 있다면), a -> b(a, b)를 G에 1로 저장
    4. G 출력
"""
import sys
input = sys.stdin.readline

N = int(input())
G = [list(map(str, input().split())) for _ in range(N)]

for k in range(N):
    for a in range(N):
        for b in range(N):
            if G[a][k] == '1' and G[k][b] == '1':
                G[a][b] = '1'


for r in G:
    print(' '.join(r))