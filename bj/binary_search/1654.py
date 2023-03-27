# import sys
#
# k, n = map(int, sys.stdin.readline().split())
#
# lines = []
#
# for _ in range(k):
#     lines.append(int(sys.stdin.readline()))
#
# start, end = 1, max(lines)
#
# while start <= end:
#     mid = (start + end) // 2
#     count = 0
#
#     for line in lines:
#         count += line // mid
#
#     if count >= n:
#        start = mid + 1
#     else:
#        end = mid - 1
#
# print(end)

"""
1. 문제 이해
    1. 설명
        * K 개의 랜선을 가지고 있지만 길이가 각각 다르다.
        * 랜선을 모두 N 개의 같은 길이의 랜선으로 만들고 싶다.
        * N 개 보다 많이 만드는 것도 N 개를 만드는 것에 포함
        * 최대 랜선의 길이를 구하기
    2. 제약사항
        * 1 <= K <= 10,000
        * 1 <= N <= 1,000,000
        * 1 <= 랜선 길이 <= 2^31 - 1
2. 접근 방법
    * 여러가지 결과 중에 최대 값을 구하는 문제이므로 매개변수 탐색을 사용한다.
    * 매개변수는 최대 랜선의 길이 x 가 매개변수. x 의 길이는 검사범위에서 중간 값(mid)이고 결정 함수의 결과에 따라 x를 늘리고 줄이면서 확인 가능
    * 결정함수는 k 개의 랜선을 각각 길이 x 로 잘랐을 때, N 개의 랜선을 만들 수 있어야한다. 조건을 만족하면 true, 아니면 false
    * k 개의 랜선을 각각 길이 x 로 나눈 몫을 모두 더하고 값이 n 보다 크거나 같으면 true, 아니면 false
    * 결정함수 반환값이 true 이면 n 개 이상 만들었다는 뜻이므로 x 를 좀더 늘려봐도 된다 -> 중간 값 mid 값을 높여야한다 -> low = mid + 1
    * false 를 반환했으면 n 개 미만으로 만들었다는 뜻이므로 x 를 줄여야한다 -> mid 의 값을 더 낮춰야 한다 -> high = mid - 1
    * 이 방법으로 진행하다가 low > high 인 순간 검사를 종료한다.
3. 코드 설계
    1. K, N 입력
    2. K 만큼 선의 길이가 입력. lines 에 저장
    3. 결정함수 정의
        1. lines 를 매개변수 x로 잘랐을 때 N 개 이상이 나오면 true 반환, 아니면 false
    4. low = 0, high = 선의 길이중 최댓값
    5. low <= high 인경우 반복
        1. mid = low + high 2로 나눈 몫
        2. 결정함수에 mid 를 넣어서 반환값이 true 이면 -> low = mid + 1
        3. 반환값이 false 이면 -> high = mid - 1
    6. high 출력
"""
from sys import stdin

K, N = map(int, stdin.readline().split())
lines = []
for _ in range(K):
    lines.append(int(stdin.readline()))


def fn(param):
    count = 0
    for l in lines:
        count += l // param

    if count >= N: return True
    else: return False


low, high = 1, max(lines)

while low <= high:
    mid = (low + high) // 2

    if fn(mid): low = mid + 1
    else: high = mid - 1

print(high)








