# 정렬

import sys

N = int(sys.stdin.readline())

numbers = []

for i in range(len(str(N))):
    numbers.append(int(str(N)[i]))

numbers.sort(reverse=True)

for i in numbers:
    print(i, end="")