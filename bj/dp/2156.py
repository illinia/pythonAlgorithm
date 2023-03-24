"""
1. 문제 이해
    1. 설명
        * 포도주 잔이 일렬로 있고
        * 잔을 선택하면 모두 마셔야하고 마신 후에는 원래 위치에 놓아야한다
        * 연속으로 놓여있는 3잔을 모두 마실 수 없다
        * 1부터 n까지 번호가 붙은 n개의 포도주잔이 순서대로 테이블에 있고 각 잔에 있는 양이 주어질때 최대한 많이 마실 수 있는 값 구하기
    2. 제약사항
        * 1 <= n <= 10,000
        * 둘째줄부터 n 개의 양이 순서대로 주어진다
        * 0 <= 포도주 양 <= 1,000
2. 접근 방법
    * 이전의 선택이 현재 결과에 영향을 미치고 최대값을 구하는 문제이므로 dp 사용
    * 현재 위치에서 최댓값을 구할 때 예시
        o x o O
        x o x O
            o X
      이전 값은 이미 dp 테이블에 최댓값으로 저장되어있다고 생각
    * 점화식 dp[i] = max(
        1. dp[i - 1]
        2. dp[i - 3] + graph[i - 1] + graph[i]
        3. dp[i - 2] + graph[i]
      ), dp[1] = graph[1], dp[2] = graph[1] + graph[2]
3. 코드 설계
    1. N 입력, graph 빈 리스트 초기화
    2. N 만큼 반복하면서 graph 에 채워넣기
    3. dp 0 부터 N까지 0으로 초기화, 1, 2 번째 값은 graph 1, 2번째 값으로 저장
    4. 3 부터 N 까지 반복 i
        1. dp[i] = max(dp[i], dp[i - 1] + graph[i], dp[i - 2] + graph[i])
    5. dp[N] 출력
"""
from sys import stdin
N = int(stdin.readline())
graph = []
for _ in range(N):
    graph.append(int(input()))

dp = [0 for _ in range(N)]
dp[0] = graph[0]

if N > 1:
    dp[1] = graph[1] + graph[0]
if N > 2:
    dp[2] = max(graph[2] + graph[1], graph[2] + graph[0], dp[1])

for i in range(3, N):
    dp[i] = max(dp[i - 1], dp[i - 3] + graph[i - 1] + graph[i], dp[i - 2] + graph[i])

print(dp[N - 1])
