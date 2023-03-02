"""
1. 문제 이해
    1. 설명
        * 종류를 가진 아이템들의 조합을 구한다.
    2. 제약사항
        * 첫 번째 줄에는 테스트 케이스의 갯수가 주어진다. 1 <= 테스트 케이스 <= 100
        * 각 테스트 케이스의 첫 번째 줄에는 가진 의상의 수 0 <= n <= 30
        * 다음 n 개에 가진 의상의 이름과 종류가 공백으로 주어진다.
        * 같은 종류의 의상은 하나만 입을 수 있다.
        * 같은 이름을 가진 의상은 존재하지 않는다.
2. 접근 방법
    * 기본적으로 조합을 구하는 문제이다.
    * 종류 별로 조합을 구하되 종류에 해당하는 이름의 갯수가 여러개일 수 있으므로
      1. 모든 종류의 조합을 구해야하므로 종류 + 1 을 전부 곱해준다.(입을 수도 안 입을 수도 있기 때문)
      2. 전체에서 -1을 해준다.
3. 코드 설계
    1. 테스트 케이스 T 입력
    2. T 만큼 반복문
        1. 의상의 수 n 입력, 의상 종류 딕셔너리 생성
        2. n 만큼 반복문
            1. 의상 종류 key 가 딕셔너리에 없으면 value 1로 해서 생성
            2. 있으면 해당 value +1
        3. 결과 값 1 생성, 딕셔너리 key들을 순회하며 value 를 결과에 곱해주기
        4. 결과 -1 하고 출력
"""
from sys import stdin

# 1
T = int(stdin.readline())
# 2
for t in range(T):
    # 2-1
    n = int(stdin.readline())
    dictionary = {}
    # 2-2
    for _ in range(n):
        # 2-2-1
        name, category = map(str, stdin.readline().split())
        if category not in dictionary:
            dictionary[category] = 1
        else:
            dictionary[category] += 1
    # 2-3
    result = 1
    for k in dictionary.keys():
        result *= dictionary[k] + 1
    # 2-4
    print(result -1)