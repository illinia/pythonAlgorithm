"""
1. 문제 이해
    1. 설명
        * M, N 보다 작거나 같은 두개의 자연수 x, y 로 각 년도를 표현한다. 첫 해는 1, 1이고, 두 해는 2, 2이다.(x, y 각각 증가한다). M, N 은 마지막 해이다
        * x, y 는 몇 번째 해를 표현하는지 구하기
    2. 제약사항
        * 1 <= M, N <= 40,000
        * 1 <= x <= M, 1 <= y <= N
2. 접근 방법
    * 정답에 x 를 빼고 M 으로 나누면 나머지가 0, 정답에 y 를 빼고 N 으로 나누면 나머지가 0
    # * 식으로 표현하면 x + aM = y + bN 이고 x에 M을 계속 더한값과 y 에 N 을 계속 더한값 끼리 같은 최소의 수를 구하면 된다.
    # * 수를 계산하면서 존재하는지 확인을 해야하므로 수를 저장하는 자료구조는 딕셔너리를 사용한다.
    # * 저장 맵은 2개 쓸 필요없이 1개를 같이 사용하면서 계산 값이 없으면 저장하고 있으면 답을 찾았으므로 답을 출력
    # * 저장하기 전 계산시 최대값인 M*N 보다 작거나 같아야하고 이 조건에 만족하는 수가 없으면 -1 이 답이다
    * 특정 수에 x 를 빼고 M 으로 나눴을 때 나머지가 0이고 같은 특정 수에 y 를 빼고 N 으로 나눴을 때 나머지가 0이면 정답
    * 특정 수가 M * N 보다 작아야 한다
    * 특정 수 초기값은 x 로 하고 M 을 계속 더해준다.
    * 함수로 만들어서 값 리턴하게 설계
3. 코드 설계
    # 1. T 입력, T 만큼 반복
    # 2. 반복문 안에서 data(결과값 저장하는 딕셔너리) 선언
    # 3. 최댓값 계산(M * N)
    # 4. 특정 값 k 를 x 로 초기화
    # 5. k 가 M * N 보다 작거나 같을 때까지 반복
    #     1. k 에 x 를 빼고 M 으로 나눈 나머지가 0이고 k 에 y 를 빼고 N 으로 나눈 나머지가 0이면 K 출력, 반복 종료
    #     2. 아니면 k 에 M 을 더해준다
    # 6. 반복 종료때까지 답을 못 찾았으면 -1 출력
    1. T 입력, T 만큼 반복
    2. 함수 선언(M, N, x, y)
        1. k 선언, x 로 초기화
        2. k 가 M * N 보다 작거나 같으면 반복
            1. (k - x) % M == 0 and (k - y) % N == 0 이면 k 가 답이므로 k 를 리턴
            2. 답이 아니면 다음 반복을 위해 k 에 M 을 더해준다.
        3. 반복문 종료했지만 함수 리턴하지 않았다면 답을 못 찾았다는 뜻이므로 -1 리턴
    3. T 반복문 안에서 M, N, x, y 를 함수에 넣어서 리턴값 출력
"""
from sys import stdin


def fn(M, N, x, y):
    while x <= M * N:
        if (x - y) % N == 0:
            return x
        x += M
    return -1


T = int(input())

for _ in range(T):
    M, N, x, y = map(int, stdin.readline().split())
    print(fn(M, N, x, y))


# from sys import stdin
#
# T = int(input())
#
# for _ in range(T):
#     M, N, x, y = map(int, stdin.readline().split())
#     data = {}
#     max_value = M * N
#     result = -1
#
#     while True:
#         if x > max_value and y > max_value:
#             break
#
#         if x in data:
#             result = x
#             break
#         else:
#             data[x] = True
#
#         if y in data:
#             result = y
#             break
#         else:
#             data[y] = True
#
#         x += M
#         y += N
#
#     print(result)