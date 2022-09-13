import sys

n, m = map(int, sys.stdin.readline().split())
# 1 <= n
# m <= 100

result = 0

for _ in range(n):
    data = list(map(int, input().split()))
    result = max(result, min(data))

print(result)

# 3 3
# 3 1 2
# 4 1 4
# 2 2 2

# 2 4
# 7 3 1 8
# 3 3 3 4