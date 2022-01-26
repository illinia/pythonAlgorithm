from collections import deque

n, k = map(int, input().split())

result = []

queue = deque()
for i in range(1, n+1):
    queue.append(str(i))

while queue:
    for _ in range(k - 1):
        queue.append(queue.popleft())
    result.append(queue.popleft())

# print('<', end='')
# print()