"""
1. 설명
    * 특정한 조건이 부합할 때만 사용할 수 있는 빠른 정렬 알고리즘
    * 별도의 리스트를 선언하고 정렬에 대한 정보를 담는다는 특징
    * 0 부터 최대값까지 리스트를 선언하고 데이터를 하나씩 확인하며 데이터 값과 동일한 인덱스의 데이터를 1씩 증가시킨다.
2. 코드 설계
    1. 무작위 정수 리스트
    2. 모든 범위를 포함하는 리스트 선언(0으로 초기화)
    3. 각 데이터에 해당하는 인덱스의 값 1증가
    4. 증가된 정보들을 순회하면서 확인
"""
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

count = [0 for _ in range(max(array) + 1)]

for i in array:
    count[i] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')


# count = [0] * (max(array) + 1)
#
# for i in range(len(array)):
#     count[array[i]] += 1
#
# for i in range(len(count)):
#     for _ in range(count[i]):
#         print(i, end=' ')