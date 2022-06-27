import sys

a, b = map(int, sys.stdin.readline().split())

num_list = []

for _ in range(a):
    num_list.append(sys.stdin.readline().strip())

min_count = 99999999

for i in range(a - 8 + 1):
    for j in range(b - 8 + 1):
        count1 = 0
        count2 = 0

        for k in range(i, i + 8):
            for m in range(j, j + 8):
                if (k + m) % 2 == 0:
                    if num_list[k][m] != 'B': count2 += 1
                    if num_list[k][m] != 'W':
                        count1 += 1
                else:
                    if num_list[k][m] != 'W': count2 += 1
                    if num_list[k][m] != 'B':
                        count1 += 1
        if count1 < min_count: min_count = count1
        if count2 < min_count: min_count = count2

print(min_count)