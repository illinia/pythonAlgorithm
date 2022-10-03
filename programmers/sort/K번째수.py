array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]


def cut_sort(a, i, j, k):
    new_array = a.copy()
    sorted_array = sorted(new_array[i - 1:j])
    return sorted_array[k - 1]


answer = []
for c in commands:
    answer.append(cut_sort(array, c[0], c[1], c[2]))

print(answer)


