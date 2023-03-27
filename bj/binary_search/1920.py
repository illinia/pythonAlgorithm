"""
1. 문제 이해
    1. 설명
        * N 개의 정수가 주어질때 안에 X 라는 정수가 존재하는지 확인
    2. 제약사항
        * 1 <= N <= 100,000
        * 다음줄부터 N 개의 정수가 주어지고
        * 1 <= M <= 100,000
        * 다음줄부터 M 개의 수가 주어지는데 이 수들이 N 개의 정수안에 포함되는지 확인
        * -2^31 <= 정수 < 2^31
2. 접근 방법
    * N 개의 수를 M 번 탐색해야하므로 N^2 은 시간초과. 정렬 NLogN, 이분 탐색 LogN 으로 해결
    * 최종 시간 복잡도는 NLogN + M*LogN = (N + M)LogN < 10^9
    * N 개의 수 리스트 A 를 정렬하고, M 개의 수를 반복하면서 이분 탐색
3. 코드 설계
    1. N 입력, A 리스트에 N 개 만큼 수 입력, 정렬
    2. M 입력, numbers 리스트에 M 개만큼 수 입력
    3. result 리스트 초기화, numbers 반복 n
        1. n 이 A 에 있는지 이분탐색
        2. 있으면 result 에 1 저장, 없으면 0 저장
    4. result 리스트 요소별로 출력
"""


def binary_search(data, target):
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return data[mid]
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return None


N = int(input())
A = list(map(int, input().split()))
A.sort()

M = int(input())
numbers = list(map(int, input().split()))

result = list()

for n in numbers:
    value = binary_search(A, n)
    if value is None:
        result.append('0')
    else:
        result.append('1')

print('\n'.join(result))