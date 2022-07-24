# 브루트 포스

import sys

N = int(sys.stdin.readline())

group = list()

for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    group.append((a, b))

for i in group:
    rank = 1
    for j in group:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end= " ")