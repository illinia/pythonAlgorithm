"""
1. 문제 이해
    1. 설명
        * 직선상에 집들이 1번부터 N 번까지 순서대로 있다
        * 3가지 색중 하나로 칠해야하고 각각 칠하는 비용이 다르다
        * 앞, 뒤로 다른 색의 집이 있어야 한다.
    2. 제약사항
        * 2 <= 집의수 N <= 1,000
        * N 개의 줄에 각각 빨강, 초록, 파랑으로 칠하는 비용이 주어진다.
2. 접근 방법
    * 이전 값에 따라 현재 값이 결정되므로 dp 로 푼다.
    * 집의 수 N 이 1,000 보다 작으므로 N^2 시간으로 해결 가능하다
    * 첫 번째 집의 색을 정해야하므로 3가지 색에 대한 경우의 수 모두를 저장
    # * 두 번째 집부터 3가지 색에 대한 경우를 따져야하고 이전 집의 색을 저장해야한다.
    * 현재 집의 색 종류에 따라 계산된 결과를 dp 테이블에 저장한다. dp 테이블에 r, g, b 에 해당하는 값을 저장한다.
    * 현재 집의 색 종류에 따라, 가능한 이전 집의 dp 테이블 값 + 현재 집 비용을 dp 테이블에 현재집 색에 맞게 저장
3. 코드 설계
    1. N 입력
    2. 리스트에 N 길이 만큼 입력 수를 3개로 나눠서 dictionary 로 r, g, b를 키값으로 입력 나눈 값을 값으로 저장
    3. dp 테이블 N 길이 만큼, dictionary 에 rgb 키에 값을 비용 최댓값(987654321)으로 초기화
    4. 두번째 집 부터 rgb 반복
        1. 현재 키값과 다른 키값을 이전 순서의 dp 테이블에서 찾고
        2. 그중 비용의 최솟값 + 현재 비용, 현재 dp 테이블 비용 중 최솟값을 현재 dp 테이블 rgb 키중 하나의 값에 저장
"""
from sys import stdin

N = int(stdin.readline())
graph = []
for _ in range(N):
    r, g, b = map(int, stdin.readline().split())
    graph.append({'r': r, 'g': g, 'b': b})

dp = [{'r': 987654321, 'g': 987654321, 'b': 987654321} for _ in range(N)]
dp[0]['r'] = graph[0]['r']
dp[0]['g'] = graph[0]['g']
dp[0]['b'] = graph[0]['b']

colors = ['r', 'g', 'b']

for i in range(1, N):
    for c in colors:
        cur_value = graph[i][c]

        for diff_c in colors:
            if diff_c != c:
                dp[i][c] = min(dp[i - 1][diff_c] + graph[i][c], dp[i][c])

min_result = 987654321
for c in colors:
    min_result = min(min_result, dp[N - 1][c])
print(min_result)