"""
1. 문제 이해
    1. 설명
        * 0 과 1로만 이루어진 수를 이진수라하고
        * 이친수는 0으로 시작하지 않고
        * 1이 두번 연속으로 나타나지 않는다.
    2. 제약사항
        * 1 <= N <= 90
2. 접근 방법
    * 완전 탐색으로 접근했을 때 첫자리, 둘째자리는 10으로 고정이고 이후부터 모든 경우의 수를 계산하면 된다.
    * 예시를 만들어서 생각
        n == 1  1
        n == 2  10
        n == 3  100, 101
        n == 4  1000, 1001, 1010
        n == 5  10000, 10001, 10010, 10100, 10101
    * 뒤에 0 이 붙는 경우는 모든 경우가 가능하므로 n - 1 에 0을 붙여주면 된다
    * 뒤에 1이 붙는 경우는 01으로 강제되므로 n - 2 에 01을 붙여주면 된다
    * 따라서 점화식은 dp[n] = dp[n - 1] + dp[n - 2]
3. 코드 설계
    1. N 입력
    2. 91 만큼 길이의 dp 테이블 0으로 초기화, n == 1, 2 인 경우 1로 초기화
    3. 3 부터 90 만큼 반복하며 점화식을 코드로 만들어 테이블에 저장
    4. 테이블에서 N 번째를 찾아 반환
"""

N = int(input())
dp = [0] * (91)
dp[1] = 1
dp[2] = 1
for i in range(3, 91):
    dp[i] = dp[i - 1] + dp[i - 2]
print(dp[N])
