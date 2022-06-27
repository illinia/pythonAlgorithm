import sys
import math
from collections import Counter

N = int(sys.stdin.readline())

nums = list()

for _ in range(N):
    nums.append(int(sys.stdin.readline()))

print(round(sum(nums) / N))
print(sorted(nums)[math.floor(N / 2)])

most_common = Counter(nums).most_common()
maximum = most_common[0][1]
mode = list()

for i in most_common:
    if i[1] == maximum:
        mode.append(i[0])

print(sorted(mode)[1] if len(mode) > 1 else mode[0])

print(max(nums) - min(nums))