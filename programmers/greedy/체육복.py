# n, lost, reserve = 5, [2, 4], [1, 3, 5]
# n, lost, reserve = 5, [2, 4], [3]
n, lost, reserve = 3, [3], [1]

for i in reserve.copy():
    if i in lost:
        reserve.remove(i)

for i in reserve:
    if (i - 1) in lost:
        lost.remove(i - 1)
    elif (i + 1) in lost:
        lost.remove(i + 1)

print(n - len(lost))