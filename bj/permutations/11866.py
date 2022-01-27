from collections import deque

n, k = map(int, input().split())

queue = deque()
for i in range(1, n+1):
    queue.append(str(i))

print('<', end='')
while queue:
    for _ in range(k - 1):
        queue.append(queue.popleft())
    print(queue.popleft(), end='')

    if queue:
        print(', ', end='')

print('>')