"""
1. 문제 이해
    1. 설명
        * N 개의 문자열로 이루어진 집합 S 가 있을 때 M 개의 문자열 중에서 S 에 포함된 것이 몇개인지 구하라.
    2. 제약사항
        * 문자열 갯수 N, M 이 주어진다(1 <= N <= 10,000, 1 <= M <= 10,000)
        * 집합 S 에는 중복은 없다.
2. 접근 방법
    * N 개의 문자열을 집합으로 만들고
    * M 개의 문자열을 입력 받을 때마다 집합에 있는지 확인하고
    * 있으면 결과값 +1 해주면 될듯
3. 코드 설계
    1. N, M 입력
    2. 집합, 결과값 생성, N 개 만큼 입력
    3. M 개 만큼 반복문 돌면서 집합에 포함되어 있는지 확인
        1. 포함되어 있으면 결과값 +1
    4. 결과값 반환
"""

from sys import stdin

N, M = map(int, stdin.readline().split())

s = set()
result = 0

for _ in range(N):
    s.add(stdin.readline())

for _ in range(M):
    m = stdin.readline()
    if m in s:
        result += 1

print(result)

