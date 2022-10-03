n = 15

answer = 1

for i in range(1, int(n // 2) + 1):
    a = i
    new = n
    while new > 0:
        new -= a
        a += 1

    if new == 0:
        answer += 1

print(answer)