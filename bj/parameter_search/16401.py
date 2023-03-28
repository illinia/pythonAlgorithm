"""
1. 문제 이해
    1. 설명
        * 최대한 긴 과자를 나눠주는데, 같은 길이의 과자를 나눠줘야 한다.
        * M 명의 조카가 있고, N 개의 과자가 있을 때, 1명에게 줄 수 있는 최대 길이
    2. 제약사항
        * 1 <= M <= 1,000,000
        * 1 <= N <= 1,000,000
        * 1 <= 과자 길이 <= 1,000,000,000
2. 접근 방법
    * 길이를 달리해서 탐색하여 과자 길이 최댓값을 구하는 매개 변수 탐색
    * 매개변수는 과자 길이
    * 결정 함수는
        1. 모든 과자를 매개변수 만큼 나눠서 몫을 전체 카운트에 더하고
        2. 카운트가 M 보다 크거나 같으면 true, 적으면 false
    * 최솟값은 과자 길이 최솟값 = 1, 최댓값은 과자 길이 최댓값 = 1,000,000,000
    * 반복시 결정 함수 결과값이 true 이면 최솟값을 늘리고, false 이면 최댓값을 줄인다
3. 코드 설계
    1. M, N 입력
    2. L 리스트 초기화, 입력 받아서 과자 길이들을 저장
    3. low = 1, high = 1000000000
    4. 결정 함수 정의(param)
        1. count = 0
        2. L 반복 l
            1. count += (l // param)
        3. count >= M return true, else return false
    5. low <= high while 반복
        1. mid = (low + high) // 2
        2. 결정함수 결과값이 true 이면 low = mid + 1, else high = mid - 1
    6. high 출력
"""
M, N = map(int, input().split())
L = list(map(int, input().split()))

low = 1
high = 1000000000


def fn(param):
    count = 0
    for l in L:
        count += (l // param)
    if count >= M: return True
    else: return False


while low <= high:
    mid = (low + high) // 2

    if fn(mid): low = mid + 1
    else: high = mid - 1

print(high)