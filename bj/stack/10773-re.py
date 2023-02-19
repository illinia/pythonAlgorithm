"""
1. 문제 이해
    1. 설명
        * 첫 번째 줄에 정수 K가 주어지고, 이후 K 개의 줄에 정수가 1개씩 주어진다.
        * 정수가 0 일 경우에는 가장 최근에 쓴 수를 지우고 아니면 해당 수를 쓴다.
        * 최종적으로 적은 수의 합을 출력한다.
    2. 제약사항
        * 1 <= K <= 100,000, 0 <= 정수 <= 1,000,000
        * 합은 2^31 - 1 보다 작거나 같은 정수(int 형 사용가능)
2. 접근 방법
    * K 가 N 이므로 O(NlogN) 이하의 복잡도로 풀어야 한다.
    * 직관적으로 생각했을 때 스택을 사용하면 될 것같다.
      리스트 사용시 append, pop O(1) 으로 총 O(N) 의 복잡도가 나온다.
3. 코드 설계
    1. 리스트로 스택 구현
    2. 입력이 0 인 경우에 대해 조건문 처리
        1. 0 인 경우 스택의 마지막 요소를 pop
        2. 0 이 아닌 경우 스택 마지막에 해당 요소를 append
    3. 스택의 모든 요소들을 순회하여 더하여 반환
"""

from sys import stdin
from collections import deque

K = int(stdin.readline())

stack = deque()

for _ in range(K):
    n = int(stdin.readline())
    if n == 0:
        stack.pop()
    else:
        stack.append(n)

result = 0
for i in stack:
    result += i

print(result)