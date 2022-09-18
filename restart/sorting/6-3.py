n = int(input())

data = []

for _ in range(n):
    d = input().split()
    name, age = d[0], int(d[1])

    data.append((name, age))

data = sorted(data, key=lambda x: x[1])

for i in data:
    print(i[0], end=' ')

# 2
# 홍길동 95
# 이순신 77