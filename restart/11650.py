import sys

N = int(sys.stdin.readline())

nums = list()

for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    nums.append([a, b])

nums.sort(key=lambda num: num[1])
nums.sort(key=lambda num: num[0])

print('\n'.join(map(lambda num: str(num[0]) + ' ' + str(num[1]), nums)))