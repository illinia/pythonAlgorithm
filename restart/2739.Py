import sys

N = int(sys.stdin.readline())

array = [i for i in range(1, 10)]

for i in array:
    print(N, "*", i, "=", N * i)