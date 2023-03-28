"""
1. 문제 이해
    1. 설명
        * N 일 동안 사용할 금액을 계산하고 M 번만 돈을 빼서 쓰기로 한다.
        * K 원을 인출하여 하루를 보낼 수 있으면 그대로 사용하고, 모자라면 남은 금액은 통장에 넣고 다시 k 원을 인출한다.
        * M 번 맞추기 위해서 남은 금액이 그날 사용할 금액보다 많더라도 남은 금액은 통장에 집어넣고 k 원을 인출할 수 있다.
        * k 를 최소하하여 구하기
    2. 제약사항
        * 1 <= N <= 100,000, 1 <= M <= N
        * 1 <= 금액 <= 10000
2. 접근 방법
    * N 개의 금액중 최댓값 <= k <= N 개의 리스트 총합
    * k 를 매개변수로하고 결정 함수는 인출 횟수가 M 과 비교했을 때 많으면 false, 적거나 같으면 true
    * 매일을 반복하면서 인출한 남은 돈 - 매일 필요한 돈
        * < 0 이면 다시 인출하고 남은 돈은 인출 금액 - 필요한 금액 인출 횟수 +1
        * >= 0 이면 남은 돈 = 남은 돈 - 필요한 금액
    * 인출 횟수 > M 이면 k 최소 금액을 늘리고, <= M 이면 k 최대 금액을 줄인다
    * 따라서 결정함수는 매일 반복하면서 인출 횟수를 카운트하고 카운트가 > M 이면 false, <= true
        결정함수가 false 이면 최소 금액을 늘리고
        true 이면 최대 금액을 줄인다.
3. 코드 설계
    1. N, M 입력
    2. numbers 리스트에 N 번 만큼 반복하여 필요한 값 저장
    3. low = N 개의 금액중 최댓값, high = N 개의 리스트 총합
    4. 결정 함수 정의(param)
        1. 인출 횟수 카운트 1, 인출한 남은 돈 = money
        2. numbers 반복 n
            1. money - n < 0 이면
                1. count += 1, money = param - n
            2. money - n >= 0
                1. money = money - n
        3. count > M 이면 false, count <= M 이면 true
    5. low <= high while 반복
        1. mid = (low + high) // 2
        2. 결정 함수에 mid 입력
            1. true 이면 high = mid - 1
            2. false 이면 low = mid + 1
    6. high 출력
"""
from sys import stdin
N, M = map(int, stdin.readline().split())

numbers = []
for _ in range(N):
    numbers.append(int(stdin.readline()))

low = max(numbers)
high = sum(numbers)


def fn(param):
    count = 1
    money = param

    for n in numbers:
        if money - n < 0:
            count += 1
            money = param - n
        else:
            money = money - n

    if count > M: return False
    else: return True


while low <= high:
    mid = (low + high) // 2

    if fn(mid): high = mid - 1
    else: low = mid + 1

print(low)
