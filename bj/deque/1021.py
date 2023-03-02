"""
1. 문제 이해
    1. 설명
        * N 개의 원소를 포함하는 양방향 순환 큐
        * 3가지 연산 수행 가능
            1. 첫 번째 원소를 뽑는다(제거).
            2. 첫 번째 원소를 가장 오른쪽으로 이동
            3. 마지막 원소를 가장 왼쪽으로 이동
        * 뽑으려는 원소의 위치가 주어질 때 순서대로 뽑는데 드는 연산의 최솟값 출력
    2. 제약 사항
        * 1 <= N <= 50
        * 1 <= M <= N
2. 접근 방법
    * 뽑는 원소는 뽑는 연산을 수행해야 한다.(제거)
    * 뽑는 원소의 위치가 전체 큐에서 절반 초과인지 미만인지 같은지에 따라 분기문 작성하면 될듯 싶다.
      해당 요소의 위치와 전체 큐의 길이로 계산하면 될 듯
    * 해당 원소를 뽑은 뒤에 다음 원소를 뽑는 경우에서 이미 실행한 연산은 횟수에 영향을 미치지 않는다.
      이동하는데 순서를 보장하기 때문
    * 시간 초과는 없을 듯 싶다.
3. 코드 설계
    1. N, M 입력, 1부터 N 까지의 큐 생성
    2. 뽑고자 하는 수의 리스트 입력(int 변환), 결과 카운트 생성
    3. 뽑고자 하는 수의 리스트 반복문
        1. 반복문 안에서 큐에서 뽑으려는 수의 인덱스 확인
            1. 인덱스 == 0 이면 첫 번째 연산 실행, 반복문 탈출
            2. 인덱스 >= 큐의 전체 길이 / 2 이면 세 번째 연산 실행, 결과 카운트 +1
            3. 인덱스 < 큐의 전체 길이 / 2 이면 두 번째 연산 실행, 결과 카운트 +1
    4. 결과 카운트 반환
"""

from sys import stdin
from collections import deque

# 1
N, M = map(int, stdin.readline().split())
q = deque([i for i in range(1, N + 1)])
# 2
nums = list(map(int, stdin.readline().split()))
result = 0
# 3
for n in nums:
    while True:
        # 3-1
        index = q.index(n)
        round1 = len(q) / 2
        # 3-1-1
        if index == 0:
            q.popleft()
            break
        # 3-1-2
        elif index >= round1:
            q.appendleft(q.pop())
            result += 1
        # 3-1-3
        else:
            q.append(q.popleft())
            result += 1

# 4
print(result)