"""
1. 문제 이해
    1. 설명
        * 자연수 원소로 갖는 공집합이 아닌 A, B
        * 대칭 차집합의 원소를 출력
    2. 제약사항
        * (A - B) 와 (B - A) 의 합집합을 A, B의 대칭 차집합이라 한다.
        * 1 <= 각 집합의 원소 개수 <= 200,000
        * 모든 원소의 값 100,000,000 이하(int 사용)
2. 접근 방법
    * set 자료형 사용하여 각 차집합을 구한 뒤 합한다음 원소의 갯수를 구하면 된다.
3. 코드 설계
    1. N, M 입력
    2. A, B 집합 원소 입력
    3. (A - B), (B - A) 의 합집합을 구한 뒤 원소 갯수 반환
"""

from sys import stdin

# 1
N, M = stdin.readline().split()
# 2
A = set(list(map(int, stdin.readline().split())))
B = set(list(map(int, stdin.readline().split())))
# 3
b_ = (A - B)
a_ = (B - A)

print(len(b_.union(a_)))