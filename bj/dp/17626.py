"""
1. 문제 이해
    1. 설명
        * 모든 자연수는 넷 혹은 그 이하의 제곱수의 합으로 표한할 수 있다. 따라서 문제 최댓값은 4로 생각
        * 자연수 n 이 주여졌을 때 최소 갯수의 제곱수 합을 출력
    2. 제약사항
        * 1 <= n <= 50,000
# 2. 접근 방법
#     * 주어진 수보다 작은 최대 제곱수를 구하고 구한 제곱수를 뺀다음 다시 구하는 방법 접근
#     * 제곱수 테이블을 만들어 놓고 접근하면 시간이 적게 걸릴듯 싶다. n 보다 작은 제곱수의 테이블을 만들기
#     * dp 테이블에서 가장 큰 수가 n 보다 작은 제곱수이니 처음 시작은 dp 테이블 마지막 원소부터 시작
#     * 큰 인덱스부터 반복하여 n 보다 작은 제곱수를 찾으면 n 에 해당 제곱수를 뺀 결과를 n 에 저장하고 카운트 +1
#     * 같은 제곱수를 뺄 수 있는 경우도 있으므로 반복문 안에 while 을 넣어서 찾은 제곱수가 n 보다 작으면 반복
#     * 계속 반복하여 n 이 0이 되면 종료하고 카운트 출력
# 3. 코드 설계
#     1. n 입력
#     2. dp 테이블을 리스트로 선언하고, 1부터 n의 제곱근 보다 작거나 같은 자연수까지 반복하여 제곱수를 저장
#     3. dp 테이블에서 마지막 원소부터 첫 번째 원소까지 반복
#         1. n 이 0이 되면 for 반복 종료
#         2. dp 테이블 원소가 n 보다 작거나 같으면 반복
#             1. n 에 해당 제곱수를 뺀 결과를 다시 저장
#             2. 카운트 +1
#             3. 빼고난 후에도 제곱수가 n 보다 작거나 같을 수 있으므로 해당 로직이 반복, 제곱수가 n 보다 크면 while 반복 탈출, 다음으로 작은 제곱수를 찾는 for 문 실행
#     4. 결과 출력
2. 접근 방법
    * 위의 방법은 그리디이고 그리디 방법으로는 최솟값을 구할 수없다.
    * 설명에서 최대 4개로 표현할 수 있다 했으니 최댓값 걱정 없이 dp 를 할 수 있다.
    * 특정 자연수는 제곱수 + 자연수 - 제곱수 이므로, 자연수 - 제곱수를 표현할 수 있는 최소 갯수를 구하면 된다.
    * 같은 패턴의 문제가 반복되고 계산 결과를 재사용할 수 있으므로 dp 로 해결한다.
    * 바텀 업 방식으로 1 부터 n 까지 최소 갯수를 구하면 될듯
    * 원하는 수의 최소 제곱수를 구할 때 1부터 시작하여 제곱수가 n 보다 작거나 같을 때까지 반복
        * n 보다 같거나 작은 제곱수들의 테이블을 0으로 초기화하고 기본 제곱수 값은 1로 초기화시켜 놓기
        * n 이 제곱수이면 이미 dp 테이블에 제곱수에 해당하는 값이 1로 저장되어 있으므로 해당 값이 0 인 경우에만 반복하여 값을 구하기
        * n 은 1의 제곱의 최솟값 + (n - 1)의 제곱의 최솟값으로 나타낼 수 있다. 이미 이전에 n 보다 작은 값들을 계산했기 때문에 문제 없다.
        * 1 에서 2로 +1 해줘서 2의 제곱의 최솟값  + (n - 2) 의 제곱의 최솟값으로 나타낼 수 있다. n - k 로 나타내는데 k 가 n 보다 작을 때까지 반복
        * 처음 1,2,..., k 들의 제곱은 이미 계산된 제곱수들이므로 1로 넣어주면 된다.
        * 점화식은 fn(n) = 1 + fn(n - k), k < n, if n == 제곱수: fn(n) = 1
        * 계산된 n 의 최솟값을 기존에 저장해놨던 dp[n] 의 값과 비교해서 최솟값을 저장
    * dp 반복 종료된 후 dp[n] 을 출력하면 됨
3. 코드 설계
    1. n 입력, dp 테이블 딕셔너리로 초기화
    2. 1부터 n 까지 dp 테이블 key 로 value 는 0 으로 저장, n 보다 작은 제곱수들의 값은 1로 저장
    3. 1 부터 n 까지 반복
        1. dp 테이블 값이 0 이 아니면 이미 계산된 제곱수라는 의미이므로 다음 반복 진행
        2. 반복할 변수값 1로 초기화
        3. 0 인 경우에 최솟값을 구하기 위해 모든 경우의 수를 반복해서 계산 후 저장할 것이므로 다시 반복, 조건은 증가시키면서 반복할 변수의 제곱수가 n 보다 작을 때까지
            1. 반복문 안에서 다시 0인지 확인하고 0이면 1 + dp[n - 1] 값으로 dp[n] 테이블 값 초기화
            2. 0이 아니면 한번 저장됐다는 뜻이므로 1 + dp[n - k] 와 이미 저장된 값 중 최솟값을 비교하여 최솟값 저장
            3. 반복할 변수 +1
    4. dp[n] 값 출력
"""
import math

n = int(input())
dp = {}

for i in range(0, n + 1):
    dp[i] = 0

for i in range(1, math.ceil(math.sqrt(n)) + 1):
    dp[i ** 2] = 1

for i in range(2, n + 1):
    if dp[i] == 0:
        count = 1
        while count ** 2 < i:
            if dp[i] == 0:
                dp[i] = 1 + dp[i - 1]
            else:
                dp[i] = min(dp[i], 1 + dp[i - count ** 2])
            count += 1

print(dp[n])

# import math
# n = int(input())
#
# dp = []
# count = 0
#
# dp_element = 1
# while dp_element <= math.sqrt(n):
#     dp.append(dp_element ** 2)
#     dp_element += 1
#
# for i in range(len(dp) -1, -1, -1):
#     if n == 0:
#         break
#
#     dp_value = dp[i]
#     while dp_value <= n and n > 0:
#         n -= dp_value
#         count += 1
#
# print(count)