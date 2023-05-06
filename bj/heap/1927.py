"""
1. 문제 이해
    1. 설명
        * 최소 힙을 이용하여 아래 연산을 지원하는 프로그램을 작성하기
            1. 배열에 자연수 x를 넣는다.
            2. 배열에서 가장 작은 값을 출력하고 그 배열에서 제거한다.
        * N 개의 줄에 정수 x가 주어지는데, x 가 자연수이면 배열에 x라는 값을 넣는 연산이고, x 가 0이라면 배열에서 가장 작은 값 을 출력하고 제거하는 경우
        * 입력에서 0 이 주어진 횟수만큼 답을 출력하라. 배열이 비어있는데 꺼내는 경우 0을 출력
    2. 제약사항
        * 1 <= 연산의 갯수 N <= 100,000
        * 0 <= x < 2^31
2. 접근 방법
    * 파이썬 내장 라이브러리인 heapq 를 사용하여 최소 힙을 구현 가능하다.
    * 최대 100,000 개의 연산을 하면 O(NLogN) 이므로 10억 미만이어서 시간안에 가능
    * N 번 반복하여 입력된 수가 0이면 힙에서 최솟값을 꺼내 존재하면 출력 없으면 0을 출력, 0이 아니면 해당 값을 입력
3. 코드 설계
    1. N 입력
    2. 힙 리스트 생성
    3. N 만큼 반복
        1. 정수 x 입력
        2. x가 0이면, 힙에서 최솟값 꺼내어 출력, IndexError(힙이 비었는데 꺼내려고 한 경우)에러가 뜨면 0 출력
        3. 0이 아니면, 힙에 x 값 추가
"""
import heapq
import sys
input = sys.stdin.readline

answer = list()
N = int(input())
h = []

for _ in range(N):
    x = int(input())
    if x == 0:
        # try:
        #     print(heapq.heappop(h))
        # except IndexError:
        #     print(0)
        if h:
            # print(heapq.heappop(h))
            answer.append(heapq.heappop(h))
        else:
            # print(0)
            answer.append(0)
    else:
        heapq.heappush(h, x)

print(*answer)