"""
1. 문제 이해
    1. 설명
        * N * N 칸으로 구성된 칸들이 있고 각 칸에 컴퓨터가 여러대가 있다.
        * 각 서버실의 컴퓨터 절반만 정상적으로 작동하면 작동하는 것으로 생각한다.
        * 1분마다 아래칸부터 컴퓨터가 켜질 때 몇 분이 필요할까
    2. 제약사항
        * 1 <= N <= 1,000
        * N * N 개의 칸에 각 칸의 컴퓨터의 갯수가 입력된다.
        * 한 칸의 최대 컴퓨터 갯수는 10,000,000
2. 접근 방법

"""

N = int(input())
computers = []

for _ in range(N):
    computers += list(map(int, input().split()))


def fn(minute):
    count = 0
    for c in computers:
        count += c if c < minute else minute

    total = sum(computers)
    computers_half = total // 2

    if total % 2 == 0:
        if count >= computers_half:
            return True
        else:
            return False
    else:
        if count > computers_half:
            return True
        else:
            return False


left = 0
right = 10_000_000

while left <= right:
    mid = (left + right) // 2

    if fn(mid): right = mid - 1
    else: left = mid + 1

print(left)