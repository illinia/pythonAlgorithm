"""
1. 문제 이해
    1. 설명
        * 배낭에 넣을 N 개의 물건이 있고, 각 물건은 무게 W, 가치 V 를 가진다
        * 최대 K 만큼의 무게를 넣을 수 있고 가치의 최댓값을 구하기
    2. 제약사항
        * 1 <= N <= 100
        * 1 <= K <= 100,000
        * 1 <= W <= 100,000
        * 0 <= V <= 1,000
2. 접근 방법
    * 물건을 넣을 때 이전 물건을 버리면서 현재 물건을 넣던가, 현재 물건을 넣지 말던가를 결정해야한다.
    * 현재 배낭의 허용 무게보다 넣을 물건의 무게가 더 크다면 넣지 않는다.
    * 아니면, 현재 넣을 물건의 무게만큼 배낭에서 뺀다(뺀 만큼의 최댓값은 배열에 저장되어있음). 그리고 물건을 넣는다.
    * 아니면 현재 물건을 넣지않고 이전 배낭 그대로 가지고 간다.
    * 해당 알고리즘을 사용하기 위해서 물건과, 배낭 무게 최대치에 대한 2차원 dp 테이블이 필요하다. 물건을 1차원으로, 배낭 무게 최대치를 2차원으로 선언
3. 코드 설계
    1. n(물건), k(배낭 무게 최대치) 입력
    2. 물건 배열 선언, 배열 0번째 인덱스는 [0, 0]으로 저장
    3. dp 테이블 n + 1, k + 1 로 2차원 배열로 선언. 0으로 초기화
    4. n 번만큼 물건 무게 w, 가치 v 입력받아 물건 배열에 추가
    5. 물건 배열을 반복, i
        1. 무게 최대치를 반복, j
            1. 물건 배열에서 i 번째 무게와 가치를 저장
            2. 배낭 무게 최대치가 물건 무게보다 작으면, 이전 물건의 최대값을 dp 테이블에 저장(해당 물건을 넣지 않음)
            3. 아니면, 이전 물건의 값과, 이전 물건에서 현재 물건의 무게를 뺀 가치의 최대값 + 현재 물건의 가치 중 최대값을 현재 물건의 무게 최대치에 저장
    6. 마지막 물건, 배낭의 최대값을 출력
"""
n, k = map(int, input().split())
data = [[0, 0]]
dp = [[0] * (k + 1) for _ in range(n + 1)]

for _ in range(n):
    data.append(list(map(int, input().split())))

for i in range(1, n + 1):
    for j in range(1, k + 1):
        w = data[i][0]
        v = data[i][1]

        if j < w:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)

print(dp[n][k])