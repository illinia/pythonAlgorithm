"""
1. 문제 이해
    1. 설명
        * N + 1 개의 I 와 N 개의 O 으로 이루어진 I, O 가 교대로 나오는 문자열을 Pn 이라한다.
        * P1 = IOI, P2 = IOIOI
        * I, O 로만 이루어진 문자열 S 와 정수 N 이 주어졌을 때 S 안에 Pn 이 몇 군데 포함되는지 구하는 프로그램을 작성하기
        * S 는 전체 문자열, M 은 문자열의 길이
    2. 제약사항
        * 1 <= N <= 1,000,000
        * 2N + 1 <= M <= 1,000,000
2. 접근 방법
    * 단순히 찾는 문자열을 S에서 슬라이싱으로 검색하면 문자열 길이(2N + 1) * M 만큼 시간이 필요하므로 시간초과가 난다
    * M 은 줄일 수 없으므로 N 을 줄여야한다.
    * 한 번에 검색하는 문자열 길이를 줄여서 반복 검색시 3 * M 시간이 필요하다. 시간초과 안난다
    * I 로 시작하는 문자열을 발견시 다음 2개의 문자를 슬라이싱해서 검색하여 OI 일 경우에 카운트에 +1을 해줘서 Pn 임을 저장한다.
    * 카운트 로직 실행 후 카운트와 N 이 일치하는지 비교하여 원하는 길이의 문자열인지 확인한다.
    * 일치하는 경우 결과값에 +1 해주고 카운트 -1하여 이후에 또 같은 패턴이 올 경우 한번 더 결과값에 더할 수 있도록 한다. 그리고 커서를 +2 해줘서 필요없는 검색을 방지.
    * 일치하지 않으면 계속 진행
3. 코드 설계
    1. N, M, S 입력, S 는 배열로 입력받기
    2. 커서 변수 선언하고 S 를 0 부터 탐색할 것이므로 0으로 초기화. 출력용 결과 변수 0 으로 초기화, 일치하는 문자열 카운트용 변수 0으로 초기화
    3. 커서가 M - 2 보다 같거나 작을 때 까지 반복
        1. S 배열에서 커서 위치에 해당하는 원소가 I 이면 다음 문자열 2개를 슬라이싱해서 한번에 가져온다.
        2. 가져온 문자열이 OI 인 경우 카운트에 +1 해준다.
            1. 카운트 로직이 실행되면 카운트와 N 이 일치하는지 비교
            2. 일치하면 결과값에 +1 해주고 카운트 변수에 -1
            3. 일치여부 상관없이 다음 2개의 문자열을 계속 탐색하게 해야하므로 커서 +2하고 계속 반복
        3. OI 가 아니면 카운트 0으로 초기화, 커서에 +1 해줘서 다음 문자열 탐색
    4. 결과값 출력
"""
N = int(input())
M = int(input())
S = list(input())

cursor = 0
result = 0
count = 0

while cursor <= M - 2:
    if S[cursor] == 'I':
        next_str = ''.join(S[cursor + 1:cursor + 3])

        if next_str == 'OI':
            count += 1
            if count == N:
                result += 1
                count -= 1
            cursor += 2
            continue
    count = 0
    cursor += 1

print(result)