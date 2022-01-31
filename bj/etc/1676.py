import sys, math

n = int(sys.stdin.readline())

N = math.factorial(n)

_list = list(str(N))
_list = list(reversed(_list))

count = 0

for i in _list:
    if i == '0':
        count += 1
    else:
        break

print(count)