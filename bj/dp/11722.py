"""
1. 문제 이해
    1. 설명
        * 수열에서 가장 긴 감소하는 부분 수열을 구하기
    2. 제약사항
        * 1 <= 수열 크기 N <= 1,000
        * 1 <= 수열 요소 <= 1,000
2. 접근 방법
    * N 이 1,000 까지므로 N^2 까지로 풀 수 있다.
    * 현재 요소의 최댓값을 dp 테이블에 저장
    * 현재 요소 앞의 요소들 중 현재 요소보다 큰 경우에, 이전 요소의 dp 값 + 1(현재 요소 포함) 과 현재 요소 dp 값 중 큰 값을 저장
    * dp[i] = max(dp[j] + 1, dp[i])
    * dp 테이블은 수열 크기 + 1 만큼 길이로 1 로 초기화
3. 코드 설계
    1. N 입력, A 입력
    2. N + 1 만큼의 dp 테이블 1로 초기화
    3. 수열 반복
        1. 현재 값의 이전 값들 반복
            1. 현재 요소가 앞의 반복 요소보다 작은 경우
            2. 현재 요소 dp 값에 이전 요소 dp 값 + 1, 현재 요소 dp 값 중 큰 값을 저장
    4. dp 테이블 최댓값 출력
"""
N = int(input())
A = list(map(int, input().split()))

dp = [1] * (N + 1)

for i in range(0, N):
    for j in range(0, i):
        if A[i] < A[j]:
            dp[i] = max(dp[j] + 1, dp[i])

print(max(dp))