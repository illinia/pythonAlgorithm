import math
from itertools import combinations

nums = [1,2,3,4]

d = sorted(nums, reverse=True)

m = d[0] + d[1] + d[2]

p = [True] * (m + 1)
p[0] = False
p[1] = False

for i in range(2, int(math.sqrt(m) + 1)):
    for j in range(i + i, m + 1, i):
        p[j] = False

c = list(combinations(d, 3))

print(c)

answer = 0
print(p)

for i in c:
    a = i[0] + i[1] + i[2]
    if p[a] == True:
        answer += 1

print(answer)