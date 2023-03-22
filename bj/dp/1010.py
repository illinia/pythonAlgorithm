"""
1. 문제 이해
    1. 설명
        * 서쪽에 N 개의 사이트, 동쪽에 M 개의 사이트
        * 서쪽과 동쪽을 연결한다. 한 사이트에 한개만 연결할 수 있다.
        * 최대한 많이 연결한다. 다리는 서로 겹쳐질 수 없다.
    2. 제약사항
        * 0 < N <= M < 30
2. 접근 방법
    * 조합으로 풀면 될듯
3. 코드 설계
    1. 테스트 케이스 T 입력
    2. T 만큼 반복
        1. N, M 입력
        2. M 에서 N 만큼의 조합 출력
"""

import math

T = int(input())
for _ in range(T):
    N, M = list(map(int, input().split()))
    print(math.comb(M, N))