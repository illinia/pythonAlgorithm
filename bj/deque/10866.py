import sys
from collections import deque

n = int(sys.stdin.readline())

_deque = deque([])

for _ in range(n):
    command = sys.stdin.readline().split()

    if command[0] == 'push_front':
        _deque.appendleft(command[1])
    elif command[0] == 'push_back':
        _deque.append(command[1])
    elif command[0] == 'pop_front':
        if _deque:
            print(_deque.popleft())
        else:
            print(-1)
    elif command[0] == 'pop_back':
        if _deque:
            print(_deque.pop())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(_deque))
    elif command[0] == 'empty':
        if _deque:
            print(0)
        else:
            print(1)
    elif command[0] == 'front':
        if _deque:
            print(_deque[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if _deque:
            print(_deque[-1])
        else:
            print(-1)