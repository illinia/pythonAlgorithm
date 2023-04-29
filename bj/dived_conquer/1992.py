"""
1. 문제 이해
    1. 설명
        * 0 과 1로 이루어진 2차원 배열을 압축하여 표현할 수 있다.
        * 모두 0으로만 되어있으면 0, 1로만 되어있으면 1, 섞여있으면 4분면으로 나누어 괄호로 묶어서 표현
        * N 은 영상의 크기, 문자열은 0 혹은 1로 들어온다
    2. 제약사항
        * 1 <= N <= 64, N 은 언제나 2의 제곱수
2. 접근 방법
    * 같은 구조를 가진 부분들로 나누어 해결할 수 있으므로 분할 정복을 사용한다. dfs 재귀함수로 해결
    * dfs 에 배열과 시작위치(x, y), 탐색할 길이를 넘겨준다.
    * 탐색할 길이가 1이면 요소가 1개인 2차원 배열이므로 해당 문자를 그냥 리턴(종료 조건)
    * 배열 파라미터를 완전 탐색하여 전부 같은 종류의 문자인지 확인하고
        1. 같은 종류라면 해당 문자를 리턴
        2. 다르면 리턴할 문자열을 (로 초기화하고
        3. 사분면을 나눠서 x, y, 길이를 계산하여 사분면에 맞게 dfs 함수 실행하고
        4. 사분면 탐색 후 리턴 받은 값을 리턴할 문자열에 더하고
        5. 사분면 탐색 종료하면 문자열에 )를 붙여 리턴
        6. 최종적으로 호출한 스코프에서 출력
3. 코드 설계
    1. N 입력, 배열 선언
    2. N 만큼 반복하며 배열을 입력받아 배열에 추가
    3. dfs 함수 정의(시작 x, y, 탐색 길이(최상위 함수에서는 N))
        1. 탐색 길이가 1이면 해당 x, y 값을 그대로 리턴
        2. 아니면 탐색용 문자열 변수에 배열 탐색 시작 위치 값을 저장, 같은 문자열인지 확인하는 플래그 True 초기화
        3. 배열 파라미터 완전탐색하여 탐색용 문자열 변수와 비교하여 하나라도 다른 값이 발견되면 플래그 False, 반복문 탈출
        4. 플래그가 True 이면 해당 탐색용 문자열 변수를 리턴하고 함수 종료
        5. 플래그가 False 이면 리턴할 문자열 ( 로 초기화, next_length 를 현재 탐색 길이(length) // 2 로 저장(사분면 탐색용 길이)
        6. 사분면으로 나눠서 dfs 함수 실행할 수 있게
            1. 1사분면 x = x, y = y, length = next_length
            2. 2사분면 x = x + next_length, y = y, length = next_length
            3. 3사분면 x = x, y = y + next_length, length = next_length
            4. 4사분면 x = x + next_length, y = y + next_length, length = next_length
            5. 해당 값들로 다시 dfs를 순서대로 실행하고 리턴값을 리턴할 문자열에 더하기
        7. 4사분면까지 완료되면 리턴할 문자열에 ) 를 더하여 리턴
    4. 리턴된 값 출력
"""
from sys import stdin

N = int(stdin.readline())
data = [list(stdin.readline()) for _ in range(N)]


def dfs(x, y, length):
    if length == "1":
        return data[y][x]

    search_string = data[y][x]
    is_same_strings = True

    for i in range(y, y + length):
        for j in range(x, x + length):
            if data[i][j] != search_string:
                is_same_strings = False
                break

    if is_same_strings:
        return search_string

    return_string = "("
    next_length = length // 2

    return_string += dfs(x, y, next_length)
    return_string += dfs(x + next_length, y, next_length)
    return_string += dfs(x, y + next_length, next_length)
    return_string += dfs(x + next_length, y + next_length, next_length)

    return_string += ")"

    return return_string


print(dfs(0, 0, N))