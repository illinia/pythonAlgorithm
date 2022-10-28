# rows = 6
# columns = 6
# queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]

rows = 3
columns = 3
queries = [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]

# rows = 100
# columns = 97
# queries = [[1,1,100,97]]

import copy

n_list = [[j for j in range(i * columns + 1, (i + 1) * columns + 1)] for i in range(rows)]

answer = []

for q in queries:
    new_list = copy.deepcopy(n_list)
    q = [i - 1 for i in q]
    y1, x1, y2, x2 = q
    small = n_list[y1][x1]

    for i in range(x1 + 1, x2 + 1):
        new_list[y1][i] = n_list[y1][i - 1]
        small = min(small, n_list[y1][i - 1])

    for i in range(y1 + 1, y2 + 1):
        new_list[i][x2] = n_list[i - 1][x2]
        small = min(small, n_list[i - 1][x2])

    for i in range(x2 - 1, x1 - 1, -1):
        new_list[y2][i] = n_list[y2][i + 1]
        small = min(small, n_list[y2][i + 1])

    for i in range(y2 - 1, y1 - 1, -1):
        new_list[i][x1] = n_list[i + 1][x1]
        small = min(small, n_list[i + 1][x1])

    answer.append(small)
    print(n_list)
    n_list = new_list

print(answer)