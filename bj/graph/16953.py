"""
1. 문제 이해
    1. 설명
        * 정수 A 를 B 로 바꾸려고 한다.
        * 가능한 연산은 두가지로 2를 곱하거나 1을 수의 가장 오른쪽에 추가하기
        * 바꾸는데 필요한 연산의 최솟값 구하기
        * 필요한 연산의 최솟값에 1을 더하여 출력, 만들 수 없는 경우 -1 출력
    2. 제약사항
        * 1 <= A <= B <= 10^9
# 2. 접근 방법
#     * 0 부터 10^9 까지 범위의 리스트를 만들고 0으로 초기화
#     * 최솟값 탐색 문제이므로 bfs 로 탐색하고, 연산 결과를 방문 리스트에 저장
#     * 연산 후에 큐에서 가져온 값이 B 와 같은지 확인하는 방법으로 최솟값 구하기
# 3. 코드 설계
#     1. A, B 입력
#     2. 방문 리스트를 0 부터 10^9까지 1으로 초기화
#     3. bfs 함수 정의
#         1. 큐 생성, 큐에 A 추가
#         2. 큐가 빌때까지 반복
#             1. 연산 결과 2가지를 B 와 비교, 같으면 연산 전의 값의 방문 값에 + 1하여 반환
#             2. 다르면 연산 결과 2개를 방문 리스트에 연산 전 값 + 1하여 저장
#             3. 큐에 큰 값을 먼저 추가
#         3. 큐가 빌때까지 반복 후에도 반환되지 않았다면 -1 반환
2. 접근 방법
    * 메모리 초과나서 다시 생각
    * 2를 곱하거나 오른쪽에 1을 추가하는 방법으로는 계산이 빠르게 끝날 것이므로 모든 경우를 저장하는 리스트를 만들 필요는 없음
    * 연산 결과를 방문확인을 사전형에 key 로 value 는 이전 연산 횟수 + 1 해서 저장하면 될듯
    * 연산 후에 방문 사전에 key 가 있는지 확인하고 있으면 해당 value + 1 반환
3. 코드 설계
    1. A, B 입력
    2. 방문 사전을 초기화, A 연산 값을 저장(1)
    3. bfs 함수 정의
        1. 큐 생성, 큐에 A 추가
        2. 큐가 빌 때까지 반복
            1. 연산 결과 2가지를 B 와 비교, 같으면 연산전의 방문 값을 방문 사전에서 가져와 +1 하여 반환
            2. 다르면 연산 결과 2개를 방문 사전에 key 값으로 연산 전 연산 횟수 + 1을 value 로 저장
            3. 제약사항에 맞는 결과만 큐에 연산 결과 2개를 추가
        3. 큐가 빌때까지 반환되지 않았다면 -1 반환
"""
from collections import deque

A, B = map(int, input().split())
visited = dict()
visited[A] = 1


def bfs():
    queue = deque()
    queue.append(A)

    while queue:
        cur_value = queue.popleft()
        cur_time = visited[cur_value]

        multiple_value = cur_value * 2
        if multiple_value == B:
            return cur_time + 1

        plus_value = int(str(cur_value) + '1')
        if plus_value == B:
            return cur_time + 1

        visited[multiple_value] = cur_time + 1
        visited[plus_value] = cur_time + 1

        if multiple_value <= 10 ** 9:
            queue.append(multiple_value)
        if plus_value <= 10 ** 9:
            queue.append(plus_value)

    return -1


print(bfs())




# from collections import deque
#
# A, B = map(int, input().split())
#
# visited = [1] * (10 ** 9 + 1)
#
#
# def bfs():
#     queue = deque()
#     queue.append(A)
#
#     while queue:
#         cur_value = queue.popleft()
#         cur_time = visited[cur_value]
#
#         multiple_result = cur_value * 2
#         if multiple_result == B:
#             return cur_time + 1
#
#         plus_result = int(str(cur_value) + '1')
#         if plus_result == B:
#             return cur_time + 1
#
#         visited[multiple_result] = cur_time + 1
#         visited[plus_result] = cur_time + 1
#
#         queue.append(multiple_result)
#         queue.append(plus_result)
#
#     return -1
#
#
# print(bfs())