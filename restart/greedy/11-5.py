n, m = map(int, input().split())
data = list(map(int, input().split()))
# data.sort()
#
# count = []
#
# for i in range(len(data)):
#     for j in range(len(data)):
#         a, b = data[i], data[j]
#         if i != j and (a, b) not in count and (a, b) not in count:
#             count.append((a, b))
#
# print(len(count))

array = [0] * 11

for x in data:
    array[x] += 1

result = 0

for i in range(1, m + 1):
    n -= array[i]
    result += array[i] * n

print(result)

# 5 3
# 1 3 2 3 2

# 8 5
# 1 5 4 3 2 4 5 2