"""
1. 문제 이해
    1. 설명
        * 정수 배열에 연산을 할 수 있고 R(뒤집기), D(버리기) 가 있다
        * R 은 배열의 수를 뒤집는 함수이고, D 는 첫 번째 수를 버리는 함수이다. 배열이 비었는데 D 를 사용한 경우 에러가 발생한다.
    2. 제약사항
        * 테스크 케이스 1 <= T <= 100
        * 함수 문자열 길이 1 <= p <= 100,000
        * 배열에 있는 수의 갯수 0 <= n <= 100,000
2. 접근 방법
    * 함수는 배열 뒤집기와 처음 수 버리기만 있고, 배열 뒤집기 함수를 매번 실행하면 시간초과가 날것이다
    * R 이 실행되어야 할때 실제로 뒤집지 않고 뒤집은 플래그만 변경하고 플래그에 따라 D 명령이 처음 수를 버릴지 뒤의 수를 버릴지 계산하면 될듯
    * Deque 를 사용하면 처음 수와 마지막 수를 버리는 시간 복잡도가 O(1) 이므로 테스크 케이스(100) * 함수 문자열 길이(100,000 * O(1)) 를 해도 시간초과가 안난다.
    * 버리기 전에 배열 길이를 체크하고 길이가 0이면 error 문자열을 출력하게 로직 추가
    * 필요한 내용
        1. AC 라는 함수를 만들고 숫자 문자열 배열과 실행할 함수 문자열을 파라미터로 받기
        2. 뒤집는 플래그 변수를 함수 안에 정의하고 해당 플래그 값은 뒤집는 함수가 실행되면 바뀌고, 값에 따라 D 함수 실행 위치가 바뀐다
        3. D 함수 실행 전에 배열 길이를 확인하고 0 이면 error 라는 문자열을 리턴하고 함수 종료
        4. 함수 실행이 전부 완료되면 R 플래그 값에 따라 배열을 뒤집어주고 해당 배열을 그대로 반환
        5. 입력시 문자열을 파싱하여 배열로 만들어주는 작업 필요
3. 코드 설계
    1. 테스트 케이스 T 입력, T 만큼 반복
    2. AC 함수 정의(배열, 함수 문자열 파라미터 받기)
        1. is_reversed 변수를 False 로 초기화
        2. 숫자 문자열을 deque 로 만들고 배열 요소 순회
            1. 요소가 R 이면 is_reversed 값 반대값을 저장
            2. 요소가 D 이면 배열 길이를 확인
                1. 길이가 0 이면 error 문자열 리턴
                2. 길이가 0 이상이고, is_reversed 가 False 이면 첫 번째 요소 제거, True 이면 마지막 요소 제거
        3. 배열 요소 순회가 정상적으로 완료되었으면 is_reversed 가 True 이면 배열을 뒤집어주고 해당 배열을 리턴
    3. T 만큼 반복
        1. 함수 문자열 p, 배열에 들어갈 수의 갯수 n 입력
        2. 배열 문자열 입력, 입력된 문자열에서 양 옆 괄호 제거하고 콤마를 기준으로 문자들을 나눠서 배열에 저장
        3. Ac 함수에 배열과 함수 문자열 넣어서 실행한 결과를 출력
"""
from collections import deque

T = int(input())


def AC(num_list, f_str):
    is_reversed = False

    f_list = list(f_str)
    if num_list == ['']:
        num_list = []
    arrays = deque(num_list)

    for i in range(len(f_list)):
        f = f_list[i]
        if f == 'R':
            is_reversed = not is_reversed
        else:
            if len(arrays) == 0:
                raise ValueError
            elif not is_reversed:
                arrays.popleft()
            else:
                arrays.pop()

    if is_reversed:
        arrays.reverse()

    return list(arrays)


for _ in range(T):
    try:
        p = input()
        n = int(input())

        # if strip == '':
        #     raise ValueError
        s = input()
        num_list = s.strip('[').strip(']').split(',')
        print('[', ','.join(AC(num_list, p)), ']', sep='')
    except ValueError:
        print('error')

