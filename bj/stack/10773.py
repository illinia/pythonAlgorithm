n = int(input())

nums = []

for _ in range(n):
    nums.append(int(input()))

stack = []

for i in nums:
    if i == 0:
        stack.pop()
    else:
        stack.append(i)

print(sum(stack))