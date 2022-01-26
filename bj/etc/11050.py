from itertools import combinations

n, k = map(int, input().split())

nums = [0] * n

print(len(list(combinations(nums, k))))
