# ex = [6, 10, 2]
n = [3, 30, 34, 5, 9]

result = sorted(list(map(str, n)), reverse=True, key=lambda x: x * 3)
print(str(int(''.join(result))))