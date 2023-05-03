"""
1. 문제 이해
    1. 설명
        * 명령어를 이용하는 계산기가 있다. 0 이상 10,000 미만의 십진수를 저장할 수 있다. 각 명령어는 저장된 n 을 변환한다.
            1. D: n 을 두배로 바꾼다. 결과가 10,000 이상인 경우에는 10,000 으로 나눈 나머지로 저장한다. (2n mod 10,000)
            2. S: n 에서 1을 뺀 결과 n-1 을 저장, n 이 0 이면 9999 가 저장된다.
            3. L: n 의 각 자릿수를 왼편으로 회전시켜 결과를 저장. 첫 번째 숫자가 가장 마지막으로 이동한다.
            4. R: n 의 각 자릿수를 오른편으로 회전시켜 결과를 저장.
        * 서로 다른 두 정수 A, B 에 대하여 최소한의 명령으로 같게 만드는 프로그램을 작성한다.
        * 자릿수로 0 이 포함된 경우도 생각해야 한다.
    2. 제약사항
        * A != B, A 는 초기값, B 는 최종값
        * A, B 는 모두 0 이상 10,000 미만
        * 최소한의 명령어 나열을 출력하는데 답이 여러가지면 아무거나 출력
2. 접근 방법
    * 최소 명령을 구하고 이전 결과의 경우의 수 중 최솟값만 원하므로 dp 보다는 bfs 로 푸는게 적합할 듯 싶다.(이전 케이스가 현재 케이스에 영향을 안줌)
    * 최소 명령을 구하는데 중복되는 답이 있을 경우 아무거나 출력하면 맞다고 하므로 답의 길이만(최소) 중요하다. 따라서 최초 방문이 최소 길이므로 리스트 대신 집합을 사용하여 시간 줄이자.
    * 큐에 들어가는 정보는 계산된 값, 추가된 명령어 2개
    * D : (2 * n) % 10_000
    * S : n - 1 if n > 0 else 9999
    * L : 자릿수 회전시 4자리 미만일 경우와, 특정 자리에 0 이 포함된 경우도 생각해야 한다.
        1. 4자리 미만일 경우 가장 앞의 자리를 구하는 법은 n // 1_000
        2. 가장 앞의 자리를 제외한 수를 구하는 법은 n % 1_000
        3. 가장 앞의 자리 제외한 수 + 가장 앞의 자리 = (n % 1_000) * 10 + (n // 1_000)
    * R : 자릿수 회전시 L 과 같은 문제가 생길 수 있다.
        1. 4자리 미만일 경우 가장 뒤의 자리 구하는 법은 n % 10
        2. 가장 뒤의 자리 제외한 수를 구하는 법은 n // 10
        3. 가장 뒤의 자리 + 가장 뒤의 자리 제외한 수 = (n % 10) * 1000 + (n // 10)
    * 각 테스트 케이스마다 출력을 해야하므로 T 만큼 반복
    * 큐 반복시 조건 : 방문하지 않았으면
3. 코드 설계
    1. T 입력, T 만큼 반복
    2. A, B 입력
    3. 방문 집합 생성, A 수를 집합에 추가(방문 체크)
    4. 큐 생성, 큐에 (A, "") 추가(초깃값, 명령어 문자열)
    5. 큐 반복
        1. 현재 값, 현재 명령어 문자열을 큐에서 가져오기
        2. 임시 값 만들어 각 명령어 계산값, 명령어 문자열을 임시값에 저장
        3. D, S, L, R 명령어 순서대로 실행
            1. 계산 후 임시 변수에 저장, 명령어 임시 변수에 저장
            2. 계산 값이 B 와 같으면 임시 명령어 문자열을 출력, 큐 종료
            3. 계산 값이 방문 집합에 없으면, 방문 체크, 계산된 임시 값과 명령어 임시 문자열을 큐에 추가
"""
from collections import deque
from sys import stdin

T = int(stdin.readline())

for _ in range(T):
    A, B = map(int, stdin.readline().split())

    visited = set()
    visited.add(A)

    queue = deque()
    queue.append((A, ""))

    while queue:
        cur_value, cur_command = queue.popleft()
        tmp_value = cur_value
        tmp_command = cur_command

        # D
        tmp_value = (2 * cur_value) % 10_000
        tmp_command = cur_command + 'D'
        if tmp_value == B:
            print(tmp_command)
            break
        if tmp_value not in visited:
            visited.add(tmp_value)
            queue.append((tmp_value, tmp_command))

        # S
        tmp_value = cur_value - 1 if cur_value > 0 else 9999
        tmp_command = cur_command + 'S'
        if tmp_value == B:
            print(tmp_command)
            break
        if tmp_value not in visited:
            visited.add(tmp_value)
            queue.append((tmp_value, tmp_command))

        # L
        tmp_value = (cur_value % 1_000) * 10 + (cur_value // 1_000)
        tmp_command = cur_command + 'L'
        if tmp_value == B:
            print(tmp_command)
            break
        if tmp_value not in visited:
            visited.add(tmp_value)
            queue.append((tmp_value, tmp_command))

        # R
        tmp_value = (cur_value % 10) * 1_000 + (cur_value // 10)
        tmp_command = cur_command + 'R'
        if tmp_value == B:
            print(tmp_command)
            break
        if tmp_value not in visited:
            visited.add(tmp_value)
            queue.append((tmp_value, tmp_command))
