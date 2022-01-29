from collections import deque

t = int(input())


for _ in range(t):
    n, m = map(int, input().split())
    _list = list(map(int, input().split()))

    queue = deque([])

    for i in _list:
        queue.append(i)

    count = 1
    while True:
        if queue[0] == max(queue):
            if m == 0:
                print(count)
                break
            else:
                queue.popleft()
                count += 1
        else:
            queue.append(queue.popleft())
        if m == 0:
            m = len(queue) - 1
        else:
            m -= 1