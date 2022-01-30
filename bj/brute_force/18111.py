import sys, math

N, M, B = map(int, sys.stdin.readline().split())

_nums = []
total = B

for _ in range(N):
    i = list(map(int, sys.stdin.readline().split()))
    _nums += i
    total += sum(i)

_result_time = 200000000
_height = 0
min_height = min(_nums)
max_height = math.floor(total / (N * M))


for h in range(min_height, max_height + 1):
    _time = 0

    for i in _nums:
        if _result_time < _time:
            break
        if i < h:
            _time += h - i
        else:
            _time += (i - h) * 2

    if _time <= _result_time:
        _result_time = _time
        _height = h

print(_result_time, _height)