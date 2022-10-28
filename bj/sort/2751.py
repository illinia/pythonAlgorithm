from sys import stdin

n = int(stdin.readline())

n_list = []

for _ in range(n):
    n_list.append(int(stdin.readline()))

def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and array[left]\
                <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1

        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]

    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


quick_sort(n_list, 0, len(n_list) - 1)
n_list = list(map(str, n_list))
print("\n".join(n_list))

