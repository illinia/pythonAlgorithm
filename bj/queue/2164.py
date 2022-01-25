from collections import deque

n = int(input())

nums = deque([i + 1 for i in range(n)])

while len(nums) > 1:
    nums.popleft()
    nums.append(nums.popleft())


print(int(nums[0]))