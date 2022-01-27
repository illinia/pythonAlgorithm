import sys

k, n = map(int, sys.stdin.readline().split())

lines = []

for _ in range(k):
    lines.append(int(sys.stdin.readline()))

start, end = 1, max(lines)

while start <= end:
    mid = (start + end) // 2
    count = 0

    for line in lines:
        count += line // mid

    if count >= n:
       start = mid + 1
    else:
       end = mid - 1

print(end)