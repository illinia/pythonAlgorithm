"""
1. 문제 이해
    1. 설명
        * 큰 수부터 작은 수의 순서로 정렬해야한다. 내림차순으로 정렬하기
    2. 제약사항
        * 1 <= 수열에 속해있는 수의 갯수 N <= 500
        * 1 <= 수 <= 100,000 자연수
        * 공백으로 구분하여 출력
2. 접근 방법
    * 선택, 삽입, 퀵, 계수 정렬을 사용하여 각각 풀이
    * 선택정렬
        1. 배열을 처음부터 끝까지 순회하면서 가장 큰(내림차순) 수를 선택해 바꿔주면 됨
        2. 순회하는 수 다음 수들 부터 큰 수를 찾기
    * 삽입정렬
        1. 배열을 순회하면서 특정 값을 특정 위치에 넣어서 정렬하는 알고리즘
        2. 해당 순회중인 원소부터 배열 두번째 값 위치까지 순회하여 이전의 값과 비교하여 자리를 바꾸거나 해당 값 순회를 탈출
        3. 내림차순이므로 배열 이전의 값과 비교시 이전 값보다 크면 자리를 바꿔주면 됨
    * 퀵 정렬
        0. 배열의 길이가 0이면 재귀 탈출(시작위치가 끝 위치보다 크면)
        1. 첫 번째 원소를 피벗으로 정하고
        2. 왼쪽부터 순회하여 피벗보다 작은 수를 찾고, 오른쪽부터 순회하여 피벗보다 큰 수를 찾아서, 두 원소의 위치를 바꿔주거나
        3. 찾지 못 한 경우 피벗보다 작은 수와 피벗을 바꿔준다.
        4. 피벗이 배열 가운데 들어가며 피벗 기준으로 왼쪽에는 피벗보다 큰 수들, 오른쪽에는 피벗보다 작은 수들이 위치하고 왼쪽, 오른쪽 배열들을 다시 퀵 정렬시키면 됨
    * 계수 정렬
        1. 0 이상의 정수 배열이므로 계수 정렬을 사용할 수 있음
        2. 카운트 배열을 배열 최댓값 + 1 길이 만큼 0으로 초기화
        3. 배열 원소들을 순회하면서 해당 원소 값을 인덱스로 하여 카운트 배열에서 위치를 찾고 해당 위치 값에 +1
        4. 카운트 배열을 순회하면서 요소 갯수 만큼 출력
3. 코드 설계
    * 선택정렬
        1. 배열 처음부터 끝까지 순회를 위한 인덱스 반복, i
            1. 최소 값의 인덱스 max_index 를 i 로 초기화
            2. i 번째 이후의 값들을 순회, j
                1. j번째 값이 max_index 값 보다 크면 max_index 에 j 를 저장
            3. 순회 종료 후 i, max_index 값을 서로 바꿔주기
    * 삽입정렬
        1. 배열 두 번째 값부터 순회, i
            1. 순회중인 i 위치부터 배열의 두번째 값인 1 위치까지 -1 을 하여 순회, j
                1. j 번째 값과 j - 1 번째 값을 비교했을 때 j 번째 값이 j - 1 번째 값보다 크면 해당 값들을 바꾸고 계속 순회
                2. 같거나 작으면 j 순회 탈출
    * 퀵 정렬
        1. 퀵정렬 정의(배열, 시작, 끝)
            1. 시작이 끝보다 크면 재귀 탈출
            2. 첫 번째 원소 위치를 피벗 위치로 정하기
            3. 왼쪽을 피벗 다음 인덱스, 오른쪽을 배열 마지막 인덱스 초기화
            4. 왼쪽이 오른쪽보다 작거나 같으면 반복
                1. 왼쪽 인덱스가 배열 끝 인덱스보다 작거나 같고, 왼쪽 값이 피벗 값보다 크거나 같으면 반복(작은 값을 찾을 때까지 반복)
                    1. 반복시에는 왼쪽 인덱스 값에 1 더하기(왼쪽에서 오른쪽으로 탐색)
                2. 오른쪽 인덱스가 배열 피봇 인덱스보다 크고, 오른쪽 값이 피벗 값보다 작거나 같으면 반복(큰 값을 찾을 때까지 반복)
                    1. 반복시에는 오른쪽 인덱스 값에 -1 하기(오른쪽에서 왼쪽으로 탐색)
                3. 탐색 종료 후 왼쪽 인덱스와 오른쪽 인덱스가 엇갈리지 않은 경우
                    1. 해당 요소들을 바꿔준다.
                4. 엇갈린 경우
                    1. 피봇값과 오른쪽값(피봇보다 큰 값)을 서로 바꿔준다.
            5. 피봇 위치 기준으로(오른쪽 값과 바꿔주었으나 인덱스는 그대로이므로 오른쪽 인덱스 기준) 배열 시작부터 피봇 위치 -1 까지, 피봇 위치 +1 부터 배열 끝까지 퀵정렬 재귀
    * 계수 정렬
        1. 카운트 배열을 배열 최댓값 + 1 길이 만큼 0으로 초기화
        2. 배열 원소들 순회 i
            1. 카운트 배열에서 i 위치의 요소에 +1
        3. 카운트 배열 원소들 마지막부터 처음원소까지 순회 i
            1. 해당 카운트 배열 i 번째 원소만큼 순회
                1. i 를 출력
"""
array4 = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

count_list = [0] * (max(array4) + 1)

for i in array4:
    count_list[i] += 1

for i in range(len(count_list) - 1, -1, -1):
    for _ in range(count_list[i]):
        print(i, end=' ')
print()

array3 = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array, start, end):
    if start > end:
        return
    pivot = start
    left = pivot + 1
    right = end

    while left <= right:
        while left <= end and array[left] >= array[pivot]:
            left += 1
        while right > pivot and array[right] <= array[pivot]:
            right -= 1

        if left <= right:
            array[left], array[right] = array[right], array[left]
        else:
            array[pivot], array[right] = array[right], array[pivot]

    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


quick_sort(array3, 0, len(array3) - 1)
print(array3)

array2 = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array2)):
    for j in range(i, 0, -1):
        if array2[j] > array2[j - 1]:
            array2[j], array2[j - 1] = array2[j - 1], array2[j]
        else:
            break

print(array2)


array1 = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array1)):
    max_index = i
    for j in range(i + 1, len(array1)):
        if array1[j] > array1[max_index]:
            max_index = j
    array1[i], array1[max_index] = array1[max_index], array1[i]

print(array1)
