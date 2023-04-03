"""
1. 문제 이해
    1. 설명
        * 삼각형 모양의 정수 트리를 위에서 부터 내려오면서 선택된 수의 합이 최대값을 구하기
        * 내려올 때는 대각선 왼쪽, 오른쪽 중 하나만 선택할 수 있다.
    2. 제약사항
        * 1 <= 삼각형 크기 <= 500
        * 0 <= 정수인 수 <= 9999
2. 접근 방법
    * 각 줄에 있는 수를 리스트에 저장하고 층마다 인덱스를 붙여 내려올 때마다 같은 삼각형 배열과 배열인 result 를 만들고 result 리스트에 최대합을 저장하여 풀면 될듯
    * 1. 현재 값의 인덱스가 0 일 때는 result 이전 배열의 인덱스 0 인 값 + 현재 값이 최대값
      2. 현재 값의 인덱스가 해당 배열에서 마지막일 때 i result 이전 배열의 마지막 요소 + 현재값이 현재 최대값
      3. 나머지일 경우 이전 배열에서 인덱스 -1 최대값, 인덱스 최대값 중 최대값 + 현재값이 현재 최대값
3. 코드 설계
    1. n 입력, numbers 리스트 초기화
    2. n 만큼 반복하여 입력 받고 입력 리스트를 numbers 배열에 추가
    3. result 2차원 배열 초기화, value 는 빈 배열, 첫 번째 배열 값은 numbers 첫 번째 배열 값으로 저장(기본 케이스)
    4. 1 부터 n - 1 까지 반복, i
        1. 0 부터 현재 numbers 에 i 번째 배열의 길이 - 1까지 반복, j
            1. if j 가 0 일때, 현재 값의 최대값은 result i - 1 의 j(0) 번째 값 + numbers i j(0) (현재값) 이 result i 의 j(0) 번째 값
            2. elif j 가 마지막일때, 현재 값의 최대값은 result i - 1 의 j(마지막) 번째 값 + numbers i j(마지막) 현재값이 result i 의 j(마지막) 번째 값
            3. else result i - 1 에서 j - 1, j 값중 큰 값 + numbers i j(현재값) 이 현재 최대값(result i j)
    5. result[n-1]중 최대값을 출력
"""
n = int(input())
numbers = []

for _ in range(n):
    numbers.append(list(map(int, input().split())))

result = [[] for _ in range(n)]
result[0].append(numbers[0][0])

for i in range(1, n):
    for j in range(0, len(numbers[i])):
        if j == 0 :
            result[i].append(result[i - 1][j] + numbers[i][j])
        elif j == len(numbers[i]) - 1:
            result[i].append(result[i - 1][j - 1] + numbers[i][j])
        else:
            result[i].append(max(result[i - 1][j - 1], result[i - 1][j]) + numbers[i][j])

print(max(result[n - 1]))