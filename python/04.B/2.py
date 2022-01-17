m, n = map(int, input().split())

data = input().split()
data.sort()

_list = ['a', 'e', 'i', 'o', 'u']

from itertools import combinations

for password in combinations(data, m):
    count = 0
    for i in password:
        if i in _list:
            count += 1
    if count >= 1 and count <= m - 2:
        print(''.join(password))