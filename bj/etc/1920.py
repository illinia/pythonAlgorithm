import sys

n = int(input())
num1 = list(map(int, sys.stdin.readline().split()))
num1.sort()

m = int(input())
num2 = list(map(int, sys.stdin.readline().split()))


def binary_search(a, x):
    start = 0
    end = len(a) - 1

    while start <= end:
        mid = (start + end) // 2
        if x == a[mid]:
            return 1
        elif x > a[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return 0


for k in range(m):
    print(binary_search(num1, num2[k]))

# result = []
#
# for i in num2:
#     if i in num1:
#         result.append('1')
#     else:
#         result.append('0')
#
#
# print('\n'.join(result))