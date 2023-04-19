"""
1. 설명
    * 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸고, 그 다음 작은 데이터를 선택해 앞에서 두 번째 데이터와 바꾸는 과정 반복
    * N - 1 번 만큼 가장 작은 수를 찾아서 맨 앞으로 보내야하고 매번 가장 작은 수를 찾기 위해 비교 연산이 필요
    * N * (N + 1) / 2 -> O(N^2), 직관적으로 이중 반복문이 사용되었으므로 N^2 라 생각할 수 있다.
2. 코드 설계
    1. 무작위의 수의 배열이 주어졌을 때
    2. 배열의 처음부터 끝까지 순회한다, i
    3. 최소 값의 인덱스를 찾아야 하므로 min_index를 i 로 초기화
    4. i 다음 인덱스부터 배열 끝까지 순회, j
    5. j 번째 수가 min_index 보다 작으면, j를 min_index 에 저장
    6. min_index 를 찾는 순회가 끝나면 min_index 는 i + 1 부터 배열끝까지 수중 최소값의 인덱스이므로
    7. i와 min_index 의 배열안의 값을 바꿔준다
"""

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i
    for j in range(i + 1, len(array)):
        if array[j] < array[min_index]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

print(array)