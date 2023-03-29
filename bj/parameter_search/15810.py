"""
1. 문제 이해
    1. 설명
        * N 명이 풍선을 만드는데 걸리는 시간이 각각 다르다.
        * M 개의 풍선을 만드는데 최소 몇 분이 걸릴까?
    2. 제약사항
        * 1 <= N, M <= 1,000,000
        * 1 <= 걸리는 시간 <= 1,000,000
2. 접근 방법
    * M 개를 만드는데 걸리는 시간의 범위가 있고 그중 최소 시간이 필요하므로 매개변수 탐색으로 해결
    * 매개변수는 걸리는 시간
    * 걸리는 시간이 주어졌을 때 각 스태프별로 해당 시간안에 풍선을 몇개 만드는지 계산하여 총 합이 필요한 풍선의 갯수보다 같거나 커야한다.
    * 결정 함수는
        1. 각 스태프 별 만들 수 있는 풍선의 갯수 카운트 +
        2. 총 카운트 >= M 이면 true, 아니면 false
    * 최솟값을 구해야 하므로 결정함수 반환값이 true 이면 high 를 낮추고, false 이면 low 를 높인다
    * low 는 1, high 는 1,000,000
    * N 명의 스태프만큼 반복하고 탐색시 걸리는 시간은 1,000,000 을 이진탐색하는데 걸리는 시간 LogN = 20, 총 시간복잡도 = NlogN 1초에 1억이 안됨
3. 코드 설계
    1. N, M 입력
    2. A (각 스태프가 풍선을 만드는데 걸리는 시간 리스트) 입력
    3. 결정 함수 정의
        1. 카운트 0 초기화
        2. A 반복하여 전체 시간 // 스태프별 걸리는 시간 을 카운트에 더하기
        3. 카운트 >= M 이면 true, 아니면 false
    4. low = 1, high = M * max(A)
    5. low <= high while 반복
        1. mid = (low + high) // 2
        2. 결정함수에 반환값 true 면 high = mid - 1, false 이면 low = mid + 1
    6. low 출력
"""
N, M = map(int, input().split())
A = list(map(int, input().split()))


def fn(param):
    count = 0
    for a in A:
        count += (param // a)
    if count >= M: return True
    else: return False


low, high = 1, M * max(A)
while low <= high:
    mid = (low + high) // 2
    if fn(mid): high = mid - 1
    else: low = mid + 1

print(low)