"""
1. 문제 이해
    1. 설명
        * 도감에 수록된 포켓몬 갯수 N 과 맞춰야 하는 문제 M 이 주어진다
        * 이름을 말하면 번호를 출력하고, 번호를 말하면 이름을 출력해야한다.
        * 둘째 줄부터 N개의 줄에 번호가 1인 포켓몬부터 N 번에 해당하는 포켓몬까지 입력
    2. 제약사항
        * 1 <= N, M <= 100,000
        * 이름은 모두 영어, 대소문자 구분 있음
        * 1 <= 숫자 <= N, 이름은 반드시 존재
2. 접근 방법
    * 이름을 입력하면 숫자를 출력하고, 숫자를 입력하면 이름을 출력한다.
    * key, value 해시맵을 이름 key, 숫자 value, 숫자 key, 이름 value 로 총 2개의 해시맵을 만든다
    * 이름이 입력되면 번호와 이름을 저장하고 문제가 입력되면 숫자인지 문자인지 판별하여 출력
3. 코드 설계
    1. N, M 입력
    2. 문자 해시맵, 숫자 해시맵 초기화, 번호 0으로 초기화
    3. N 만큼 반복
        1. 입력 받은 이름 저장, 번호 +1
        2. 문자 맵, 숫자 맵에 각각 저장, 숫자는 저장시에 문자열로 만들어 저장
    4. M 만큼 반복
        1. 입력받은 문자와 숫자에 따라 맵에서 value 값 출력
"""
from sys import stdin

N, M = map(int, stdin.readline().split())
str_map = dict()
num_map = dict()
number = 0

for _ in range(N):
    name = stdin.readline().rstrip()
    number += 1

    str_map[name] = str(number)
    num_map[str(number)] = name

for _ in range(M):
    question = str(stdin.readline().rstrip())

    if question.isalpha():
        print(str_map[question])
    else:
        print(num_map[question])

