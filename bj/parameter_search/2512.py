"""
1. 문제 이해
    1. 설명
        * 총액 이하에서 최대의 총 예산을 배정한다.
            모든 요청이 배정될 수 있으면 그대로 배정
            아닐 경우 특정한 정수 상한액을 계산하여 이상인 예산 요청에는 상한액을 배정한다. 이하의 요청에는 그대로 배정
        * 상한액이나 최댓값을 반환하기
    2. 제약사항
        * 3 <= 지방의 수 N <= 10,000
        * 각 지방의 예산요청인 N 개의 정수가 한줄에 주어짐
        * 1 <= 예산 요청 액 <= 100,000
        * 총 예산 M, N <= M <= 1,000,000,000
2. 접근 방법
    * 여러가지 결과중에 최댓값을 구하는 문제는 매개변수 탐색을 사용한다.
    * 매개변수는 x (상한액)
    * 가장 낮은 상한액은 요청 액수중 최솟값, low
    * 가장 높은 상한액은 요청 액수중 최댓값, high
    * 결정함수는
        1. 상한액 보다 큰 예산인 경우 상한액
        2. 작은 예산인 경우 예산
        3. 값들을 더한 값이 총 예산 보다 작거나 같으면 True, 아니면 False
    * low <= high 인 조건으로 while 반복
        * 결정함수 반환값이 True 인 경우 상한액을 좀 더 늘려봐도 되므로 low = mid + 1
        * False 인 경우 상한액을 줄여야하므로 high = mid - 1
    * 반복문 종료 후 high 값 출력
3. 코드 설계
    1. N 입력
    2. numbers 리스트 초기화, N 개의 수 입력, M 입력
    3. low, high 초기화
    4. 결정 함수 정의
        1. 총 합을 저장하는 수 초기화
        2. numbers 순회하면서, 상한액보다 큰 경우 상한액으로 총 합에 저장, 작거나 같은 경우 해당 값을 총 합에 저장
        3. 총 합이 총 예산보다 작거나 같으면 True 반환, 아니면 False 반환
    5. low <= high while 반복
        1. mid = low, high 더한 값의 2로 나눈 몫
        2. 결정함수에 mid 넣어서 반환시 True 이면 low = mid + 1
        3. False 이면 high = mid - 1
    6. high 출력
"""
N = int(input())
numbers = list(map(int, input().split()))
M = int(input())

low, high = 0, max(numbers)


def fn(param):
    total = 0
    for n in numbers:
        if n > param: total += param
        else: total += n

    if total <= M: return True
    else: return False


if sum(numbers) <= M:
    print(max(numbers))
else:
    while low <= high:
        mid = (low + high) // 2

        if fn(mid): low = mid + 1
        else: high = mid - 1

    print(high)
