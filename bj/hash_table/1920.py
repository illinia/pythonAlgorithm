"""
1. 문제 이해
  1. 설명
    * N 개의 정수가 주어지고 M 개의 정수들이 주어졌을 때
    * M 개의 수들이 N 개의 정수 안에 존재하는지 알아내면 된다.
  2. 제약 사항
    * 첫 번째 입력 1 <= N <= 100,000
    * N 만큼 최소 1번은 탐색해야 하므로 시간 복잡도에 영향을 미친다.
    * O(NlogN) 으로 풀수 있음
    * 세 번째 입력 1 <= M <= 100,000
    * M 만큼 최소 1번은 탐색해야 하므로 시간 복잡도에 영향을 미친다.
    * O(NlogN) 으로 풀수 있음
2. 접근 방법
  1. 직관적으로 생각하기
    * 완전탐색은 O(N2) 이므로 시간초과
  2. 자료구조와 알고리즘 활용
    * O(NlogN) 은 사용 가능하니 정렬해도 문제없음
    * 정렬후 이분탐색 사용가능
    * 아님 N 개의 수를 해시테이블에 넣고 M 만큼 key 가 존재하는지 확인도 가능
"""

# from sys import stdin

# 해시 테이블 사용

# N = stdin.readline()
# A = list(map(int, stdin.readline().split()))
# M = stdin.readline()
# data = list(map(int, stdin.readline().split()))
#
# hash_table = dict()
#
# for a in A:
#     hash_table[a] = True
#
# result = list()
#
# for d in data:
#     if hash_table.get(d):
#         result.append('1')
#     else:
#         result.append('0')
#
# print('\n'.join(result))

# 이분 탐색 구현

from sys import stdin

N = stdin.readline()
A = list(map(int, stdin.readline().split()))
A.sort()
M = stdin.readline()
data = list(map(int, stdin.readline().split()))
result = []


def binary_search_recursion(target, data, start, end):
    if start > end:
        return '0'

    mid = (start + end) // 2

    if target == data[mid]:
        return '1'
    elif data[mid] < target:
        return binary_search_recursion(target, data, mid + 1, end)
    else:
        return binary_search_recursion(target, data, start, mid - 1)


for d in data:
    result.append(binary_search_recursion(d, A, 0, len(A) - 1))

print('\n'.join(result))

# for d in data:
#     start = 0
#     end = len(A) - 1
#     mid = (start + end) // 2
#
#     while start <= end:
#         mid_value = A[mid]
#         if mid_value == d:
#             result.append('1')
#             break
#         elif mid_value < d:
#             start = mid + 1
#         else:
#             end = mid - 1
#     result.append('0')