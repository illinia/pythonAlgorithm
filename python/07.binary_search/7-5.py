import sys

n = int(sys.stdin.readline().rstrip())

n_list = list(map(int, sys.stdin.readline().rstrip().split()))
n_list.sort()

m = int(sys.stdin.readline().rstrip())

m_list = list(map(int, sys.stdin.readline().rstrip().split()))


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


for i in m_list:
    result = binary_search(n_list, i, 0, n - 1)
    if result:
        print('yes', end=' ')
    else:
        print('no', end=' ')

# 5
# 8 3 7 9 2
# 3
# 5 7 9