import sys

n = int(input())

nums = []

for _ in range(n):
    first, second = map(int, sys.stdin.readline().split())
    nums.append([first, second])

nums = sorted(nums, key=lambda a: a[0])
nums = sorted(nums, key=lambda a: a[1])

last = 0
cnt = 0

for i, j in nums:
    if i >= last:
        cnt += 1
        last = j

print(cnt)