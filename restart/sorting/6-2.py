n = int(input())

data = []

for _ in range(n):
    data.append(int(input()))

data = sorted(data, reverse=True)

for i in data:
    print(i, end=' ')

# 3
# 15
# 27
# 12