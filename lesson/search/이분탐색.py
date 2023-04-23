"""
1. 설명
    * 정렬된 자료를 반으로 나누어 탐색하는 방법
    * 자료는 오름차순으로 정렬된 자료여야한다.
2. 접근 방법
    * 자료의 중간 값이 찾고자 하는 값인지 검사
    * 아니라면 대소관계를 비교하여 start, end 값 이동
3. 코드 설계
    1. target(찾고자 하는 값), data(오름차순으로 정렬된 List) 를 파라미터로 받는 함수 정의
    2. start 인덱스 0, end 인덱스 배열 마지막 인덱스로 초기화
    3. start 가 end 보다 작거나 같으면 반복
        1. mid 는 start, end 합을 2로 나눈 몫
        2. 중간 값이 target 과 일치하면 해당 값 반환
        3. target 보다 작으면, start 를 mid + 1 로 저장하고 다시 반복
        4. 아니면, end 를 mid - 1 로 저장하고 다시 반복
"""


def binary_search(target, data):
    start = 0
    end = len(data) - 1
    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return data[mid]
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return None


data = [i for i in range(1, 11)]
data.sort()

print(binary_search(3, data))
print(binary_search(30, data))