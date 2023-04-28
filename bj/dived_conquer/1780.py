"""
1. 문제 이해
    1. 설명
        * N*N 크기의 행렬로 표현되는 종이가 있다. 각 칸에는 -1, 0, 1 중 하나가 저장되어 있다.
        * 만약 종이가 모두 같은 수로 되어있다면 종이를 그대로 사용한다.
        * 아닌 경우에 종이를 같은 크기의 종이 9 개로 자르고 각각 잘린 종이에 대해 위의 과정을 반복한다.
        * 이렇게 잘랐을 때 -1 로만 채워진 종이의 갯수, 0 으로만 채워진 종이의 갯수, 1로만 채워진 종이의 갯수를 구하기
    2. 제약사항
        * 1 <= N <= 3^7
# 2. 접근 방법
#     * 전체를 반복해서 분할하여 해결해야하므로 분할정복을 사용한다.
#     * 분할정복 함수를 만들고 2차원 배열을 파라미터로 넣어준다.
#     * 함수 시작시 2차원 배열 길이가 1, 1인 경우에 종료 조건 걸고, 배열내 모든 원소가 같다면 종료 조건을 건다.
#     * 종료시 해당 원소에 해당하는 카운트를 +1 해준다.
#     * 모든 원소가 같지 않다면 배열을 총 9개로 나누어 다시 분할 정복한다.
# 3. 코드 설계
#     1. N 입력, 배열 선언
#     2. N 만큼 반복하여 배열에 정수 배열을 추가하여 2차원 배열로 만들기
#     3. -1, 0, 1 에 해당하는 카운트 0으로 초기화
#     4. 분할정복 함수 정의(2차원 배열 파라미터)
#         1. 배열의 길이가 1이라면 안의 원소에 해당하는 카운트 +1 해주고 리턴
#         2. 해당 함수에서 사용하는 원소 종류를 저장하기 위한 기본 변수 배열의 첫번째 값으로 초기화
#         3. 배열내 모든 값을 반복하면서 값들이 같다면 해당 원소 카운트 +1 해주고 리턴
#         4. 하나의 원소라도 값이 다르다면 2중 배열 반복 종료하고, 파라미터 배열을 9개로 나누어 다시 함수 실행
#     5. -1, 0, 1 출력
2. 접근 방법
    * 전체 배열을 파라미터로 넘겨주는게 아니라 탐색해야할 시작 위치x, y 와 배열 길이 n 을 넘겨주기로 변경
    * 처음 원소를 확인용으로 다른 변수에 저장
    * x, y 좌표를 계산(파라미터로 받은 처음 값 ~ 값 + 배열의 길이 -1)하는 2중 반복
    * 이중 반복시 저장된 원소 확인용 값과 같지 않으면 9개로 나눠서 분할 정복
    * 같지 않는 경우에 분할 정복을 실행한 2중 반복문이 끝나면 재귀 함수 자체를 return 시켜줘서 반복문 종료, 카운트 로직 실행 안하게 함수를 종료
    * 모든 반복문이 실행되었는데도 함수가 종료되지 않았다면 모든 원소의 종류가 같다는 것이고 해당 종류에 맞는 카운트 값 +1
3. 코드 설계
    1. N 입력, 배열 선언
    2. N 만큼 반복하여 배열에 정수 배열을 추가하여 2차원 배열로 만들기
    3. -1, 0, 1 에 해당하는 카운트 0으로 초기화
    4. 분할정복 함수 정의(row, col, length)
        1. 확인용 변수에 처음 원소값 저장
        2. x ~ x + length, y ~ y + length 반복
            1. 확인용 변수와 비교해서 해당 원소 값이 같으면 아무것도 안함
            2. 다르면 length 를 3으로 나눈 몫을 length 로 하여 배열을 9개로 나누어 재귀 호출
            3. 마지막에 함수 자체를 리턴하여 더이상 분할정복하지 않게 반복문 탈출, 뒤에올 카운트 로직 실행 안하게 함
            4. 반복문 전부 통과하고 함수가 종료되지 않았다면 해당원소와 같은 카운트 값 +1
        3. 카운트 값들 출력
"""
from sys import stdin

N = int(stdin.readline())
arrays = [list(map(int, stdin.readline().split())) for _ in range(N)]

result_list = [0, 0, 0]


def fn(x, y, length):
    check = arrays[x][y]

    for i in range(x, x + length):
        for j in range(y, y + length):
            if arrays[i][j] != check:
                next_length = length // 3
                fn(x, y, next_length)
                fn(x, y + next_length, next_length)
                fn(x, y + next_length * 2, next_length)
                fn(x + next_length, y, next_length)
                fn(x + next_length, y + next_length, next_length)
                fn(x + next_length, y + next_length * 2, next_length)
                fn(x + next_length * 2, y, next_length)
                fn(x + next_length * 2, y + next_length, next_length)
                fn(x + next_length * 2, y + next_length * 2, next_length)
                return

    result_list[check + 1] += 1


fn(0, 0, N)
print('\n'.join(list(map(str, result_list))))



# from sys import stdin
#
# N = int(stdin.readline())
# data = [list(map(int, stdin.readline().split())) for _ in range(N)]
#
# result_list = [0, 0, 0]
#
#
# def fn(arrays):
#     if len(arrays) == 1:
#         result_list[arrays[0][0] - 1] += 1
#         return
#
#     number = arrays[0][0]
#     all_same = True
#
#     for i in range(len(arrays)):
#         break_flag = False
#         for j in range(len(arrays[0])):
#             if arrays[i][j] != number:
#                 break_flag = True
#                 break
#
#         if break_flag:
#             all_same = False
#             break
#
#     if all_same:
#         result_list[arrays[0][0] - 1] += 1
#         return
#
#     for i in range(3):
#         for j in range(3):
#             unit_length = len(arrays) // 3
#             start_row = i * unit_length
#             end_row = (i + 1) * unit_length
#             start_col = j * unit_length
#             end_col = (j + 1) * unit_length
#             parameter = arrays[start_row:end_row][start_col:end_col]
#             print(parameter)
#             fn(parameter)
#
#
# fn(data)
# '\n'.join(list(map(str, result_list)))
