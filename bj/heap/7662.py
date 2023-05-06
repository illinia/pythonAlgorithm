"""
1. 문제 이해
    1. 설명
        * 연산 명령에 따라 우선순위가 가장 높은 데이터 혹 가장 낮은 데이터를 삭제하는 이중 우선순위 큐를 구현하라
        * 최종적으로 저장된 데이터중 최댓값과 최솟값을 출력
        * 테스트 케이스 T 가 입력되고 각 테스트 케이스 첫째 줄에는 힙에 적용할 연산의 갯수를 나타내는 정수 k가 주어진다.
        * k 번 입력시 연산을 나타내는 문자(D or I)와 정수 n 이 주어진다
        * I 는 n을 힙에 삽입하고, 동일한 정수가 삽입될 수 있다. D 1 은 힙에서 최댓값을 삭제, D -1은 최솟값을 삭제
        * 힙이 비었는데 D 연산을 해야하면 무시한다.
        * 모든 연산을 처리한 후 남아있는 최댓값, 최솟값을 구하기
2. 접근 방법
    * 최대힙, 최소힙을 각각 구현한다.
    * 최대값 삭제, 최솟값 삭제시 모든 연산 후에 두가지 힙을 동기화시켜야한다.
    * k 번 반복되는 동안 입력 순서를 이용해 방문 체크하는 리스트를 만들어 최대힙, 최소힙에서 pop 할때 다른 힙에서 제거한 요소인지 확인할 수 있다.
    * 방문한 요소(다른 힙에서 이미 방문하여 삭제한 요소)이면 힙이 비어있지 않고 방문하지 않은 요소가 나올때까지 계속 삭제
    * 힙이 비어있지 않고 방문하지 않은 요소이면 해당 힙에서 제거하고 방문 체크
    * 연산이 모두 끝난 후에도 동기화를 한번씩 더 실행
    * 최대힙과 최소힙이 비어있으면 EMPTY 출력, 아니면 최대, 최소 출력
3. 코드 설계
    1. T 입력, T 만큼 반복
    2. k 입력, k 길이 만큼 방문 체크 리스트 False 로 초기화(최대 K 번 입력될 수 있으므로), 최대, 최소힙 생성
    3. k 반복
        1. operation, n 입력
        2. operation이 I 이면 최대힙, 최소힙에 둘다 (n, k반복 횟수) 튜플로 저장
        3. D 이고 1 이면
            1. 최대힙이 비어있지 않고 가장 앞의 요소의 순서로 방문 체크했을 시 True 이면(다른 힙에서 방문했다는 뜻), 최대힙에서 최대값을 pop 한다
            2. 반복이 끝나고 최대힙이 비어있지 않으면, 마지막으로 최대힙 첫번째 요소의 순서로 방문 체크(True 저장), 최대힙에서 pop
        4. D 이고 -1 이면
            1. 최소힙이 비어있지 않고 가장 앞의 요소의 순서로 방문 체크했을 시 True 이면(다른 힙에서 방문했다는 뜻), 최소힙에서 최소값을 pop 한다
            2. 반복이 끝나고 최소힙이 비어있지 않으면, 마지막으로 최소힙 첫번째 요소의 순서로 방문 체크(True 저장), 최소힙에서 pop
    4. k 번 반복이 끝나고 최대, 최소힙 다시 동기화
    5. 최대, 최소 힙이 둘다 비어있지 않으면 최대, 최소값 출력,아니면 EMPTY 출력
"""
import heapq
import sys

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    k = int(input())
    visited = [False] * k
    min_h = []
    max_h = []

    for i in range(k):
        operation, n = input().split()
        n = int(n)

        if operation == 'I':
            heapq.heappush(min_h, (n, i))
            heapq.heappush(max_h, (-n, i))
        elif n == 1:
            while max_h and visited[max_h[0][1]]:
                heapq.heappop(max_h)
            if max_h:
                visited[max_h[0][1]] = True
                heapq.heappop(max_h)
        else:
            while min_h and visited[min_h[0][1]]:
                heapq.heappop(min_h)
            if min_h:
                visited[min_h[0][1]] = True
                heapq.heappop(min_h)
    while max_h and visited[max_h[0][1]]:
        heapq.heappop(max_h)
    while min_h and visited[min_h[0][1]]:
        heapq.heappop(min_h)


    if max_h and min_h:
        print(-heapq.heappop(max_h)[0], heapq.heappop(min_h)[0])
    else:
        print('EMPTY')