# 집합

import sys

input()

numberN = set(map(int, input().split()))

input()

numberM = list(map(int, input().split()))

for m in numberM:
    if m in numberN:
        print("1", end=" ")
    else:
        print("0", end=" ")
