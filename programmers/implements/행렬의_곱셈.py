arr1 = [
    [2, 3, 2],
    [4, 2, 4],
    [3, 1, 4]]

arr2 = [
    [5, 4, 3],
    [2, 4, 1],
    [3, 1, 1]]

result = [[0] * len(arr1) for _ in range(len(arr1))]

for i, a in enumerate(arr1):
    for j, b in enumerate(a):
        answer = 0

        for k, c in enumerate(arr2):
            answer += c[j] * a[k]

        result[i][j] = answer

print(result)
