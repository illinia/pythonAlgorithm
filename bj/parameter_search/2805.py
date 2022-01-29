import sys

n, m = map(int, sys.stdin.readline().split())

_list = sorted(list(map(int, sys.stdin.readline().split())))


def parameter_search(_list, start, end):
    if start > end:
        print(end)
        return

    mid = (start + end) // 2

    total = 0

    for i in _list:
        if i - mid > 0:
            total += i - mid

    if total >= m:
        start = mid + 1
    else:
        end = mid - 1

    parameter_search(_list, start, end)


parameter_search(_list, 0, max(_list))