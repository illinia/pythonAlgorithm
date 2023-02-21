"""
1. 문제 이해
    1. 설명
        * 숫자 N 개가 있고, 정수 M 개가 주어졌을 때 해당 정수가 N 개에서 몇개가 있는지 구하라.
        * 숫자 N 입력, 해당 N 개의 숫자가 입력, 숫자 M 입력, 해당 M 개의 숫자 입력
    2. 제약 사항
        * 1 <= N <= 500,000 -> O(NlogN) 까지 풀 수 있다.
        * -10,000,000 <= N 개의 수 <= 10,000,000 -> int 형 사용 가능
        * 1 <= M <= 500,000 -> O(NlogN)
        * -10,000,000 <= M <= 10,000,000
2. 접근 방법
    * O(NlogN) 이기 때문에 정렬 가능
      정렬 후 이분 탐색시 시간 괜찮을 듯
    * 해시 테이블에 N 개의 수를 Key 로 해당 갯수를 value 로 해서 저장시
      M 개의 수를 각각 O(1) 시간으로 조회 가능, 총 O(N) 시간 소요
3. 코드 설계
    1. 이분 탐색
        1. N 입력, N 개의 수를 리스트에 입력, 정렬
        2. M 입력, M 개의 수를 리스트에 입력(혹은 바로 조회)
        3. 결과 리스트 생성
        4. 이분 탐색 알고리즘 구현
            1. 하한, 상한 값을 구해야하기 때문에 하한, 상한 구하는 알고리즘을 각각 구현
            2. 하한시에는 검색시마다 상한 범위를 낮춰야 한다.
            3. 상한시에는 검색시마다 하한 범위를 낮춰야 한다.
        5. M 리스트를 순차 조회하면서 N 리스트를 이분 탐색(이분 탐색은 O(logN) 이므로 총 O(NlogN) 시간 소요)
            1. 상한 이분탐색에서 하한 이분탐색을 빼고 1을 더하면 해당 요소의 총 갯수가 된다.
    2. 해시 테이블
        1. N 입력, N 개의 수를 해시 테이블에 입력(key = 수, value = 조회시 마다 +1)
        2. M 입력, M 개의 수를 리스트에 입력(혹은 바로 조회)
        3. 결과 리스트 생성
        4. M 리스트를 순차 조회하면서 해시 테이블에서 value 값 가져오기(해시 테이블 조회는 O(1) 이므로 총 O(N) 시간이 걸림)
            1. 키가 존재하는지 확인
            2. 조회 성공시 해당 value 를 결과 리스트에 저장
            3. 조회 실패시 결과 리스트에 0 저장
"""

# from sys import stdin
# from collections import deque
#
# # 이분 탐색 구현
# # 1.
# N = int(stdin.readline())
# N_list = list(map(int, stdin.readline().split()))
# N_list.sort()
#
# # 2.
# M = int(stdin.readline())
# M_list = list(map(int, stdin.readline().split()))
#
# # 3.
# result = []
#
#
# # 4.
# def lower_bound_search(target, data):
#     lower, upper = 0, len(data)
#
#     while lower < upper:
#         mid = (lower + upper) // 2
#         if target <= data[mid]:
#             upper = mid
#         else:
#             lower = mid + 1
#
#     return lower
#
#
# def upper_bound_search(target, data):
#     lower, upper = 0, len(data)
#
#     while lower < upper:
#         mid = (lower + upper) // 2
#         if target < data[mid]:
#             upper = mid
#         else:
#             lower = mid + 1
#
#     return lower
#
#
# # 5.
# for m in M_list:
#     result.append(str(upper_bound_search(m, N_list) - lower_bound_search(m, N_list)))
#
# print(' '.join(result))

# 해시 테이블 구현

from sys import stdin
from collections import deque

# 1.
N = int(stdin.readline())
data = {}
for n in map(int, stdin.readline().split()):
    if n in data:
        data[n] = data.get(n) + 1
    else:
        data[n] = 1

# 2.
M = int(stdin.readline())
M_list = list(map(int, stdin.readline().split()))

# 3.
result = []

# 4.
for m in M_list:
    if m in data:
        result.append(str(data.get(m)))
    else:
        result.append('0')

print(' '.join(result))



