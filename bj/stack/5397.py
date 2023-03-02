"""
1. 문제 이해
    1. 설명
        * 입력된 문자를 이용해 정확한 문자를 구하라
        * 입력된 문자는 알파벳 대문자, 소문자, 숫자, 백스페이스, 화살표이다
    2. 제약사항
        * 1 <= 문자열 길이 <= 1,000,000
        * 백스페이스 입력시 -, 커서 앞(왼쪽)에 글자가 존재하면 글자를 지운다.
        * 화살표는 <, > 로 주어진다.
2. 접근 방법
    * 문자열을 최소 한번은 순회해야 하므로 O(NlogN) 으로 풀 수 있다.
    * 백스페이스 입력시 왼쪽 글자를 지우기 때문에 일반적인 리스트나 스택으로는 풀기 어렵다.
    * 스택을 두개 사용하여 커서 왼쪽, 오른쪽을 나누어서 생각하면 좋을 듯
    * 스택 두개 사용시 마지막 글자만 추가, 삭제하면 되므로 O(1) 걸림
    * 백스페이스, 화살표 이동도 구현 가능하다.
    * deque 사용
3. 코드 설계
    1. 테스트 케이스 갯수 N 입력, 결과 리스트 생성
    2. 케이스 갯수만큼 반복
        1. 문자열 입력
        2. 왼쪽 스택, 오른쪽 스택 생성
        3. 가장 왼쪽 문자부터 처리하게 문자열 반복
            1. < 일시, 왼쪽 스택 pop 결과를 오른쪽 스택 append
            2. > 일시, 오른쪽 스택 pop 결과를 왼쪽 스택 append
            3. - 일시, 왼쪽 스택 pop
            4. 나머지 왼쪽 스택 append
        4. 왼쪽 스택 + 오른쪽 스택 뒤집어서 더하고 결과 리스트 추가
    3. 결과 리스트 join 하여 출력
"""

from sys import stdin
from collections import deque
# 1
N = int(stdin.readline())
result = list()
# 2
for _ in range(N):
    # 2-1
    words = stdin.readline().rstrip()
    # 2-2
    lstack, rstack = deque(), deque()
    # 2-3
    for w in words:
        # 2-3-1
        if w == '<':
            if len(lstack) > 0:
                rstack.append(lstack.pop())
        # 2-3-2
        elif w == '>':
            if len(rstack) > 0:
                lstack.append(rstack.pop())
        # 2-3-3
        elif w == '-':
            if len(lstack) > 0:
                lstack.pop()
        # 2-3-4
        else:
            lstack.append(w)
    # 2-4
    result.append(''.join(lstack) + ''.join(reversed(rstack)))

# 3
for r in result:
    print(r)