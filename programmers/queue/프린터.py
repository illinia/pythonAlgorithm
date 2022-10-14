import time
from collections import deque, Counter

priorities = [1, 1, 9, 1, 1, 1]
location = 0
answer = 0

q = deque([(a, i) for i, a in enumerate(priorities)])

while q:
    n = q.popleft()

    print(q)

    if n[0] < max(q)[0]:
        q.append(n)
    else:
        answer += 1
        if location == n[1]:
            break

print(answer)