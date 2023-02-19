"""
1. 문제 이해
    1. 설명
        * N 장의 카드가 있고 1 부터 N 까지 번호가 있고
          1번 카드가 제일 위, N 번 카드가 제일 아래에 있다.
        * 제일 위에 있는 카드를 버리고
          다음 제일 위에 카드를 제일 아래에 있는 카드 밑으로 옮긴다.
    2. 제약사항
        * 입력 1 <= N <= 500,000
2. 접근 방법
    * 전체 순회 후 절반의 횟수로 다시 전체 순회
      이것을 길이가 1이 될때까지 반복
      수행 횟수는 전체 길이의 2배이다
    * O(NlogN) 으로 풀수 있을 듯
    * 직관적으로 생각했을 때 큐의 구조라 생각됨
3. 코드 설계
    1. 정수 N 을 입력 받는다.
    2. 1부터 N 까지 수를 담은 리스트를 만들어 큐에 넣는다.
    3. 전체 반복 횟수를 가지는 변수를 선언한다.
    4. 반복문 안에서 큐의 길이가 1이 될 때까지 반복한다.
    5. 최종으로 남은 요소를 출력한다.
"""

from sys import stdin
from collections import deque

N = int(stdin.readline())

q = deque([i for i in range(1, N + 1)])

index = 1

while len(q) != 1:
    if index % 2 == 1:
        q.popleft()
    else:
        pop = q.popleft()
        q.append(pop)
    index += 1

print(q.pop())
