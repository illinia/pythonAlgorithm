# N, M, K = map(int, input().split())
# number = list(map(int, input().split()))

n, m, k = 5, 8, 3
number = [2, 4, 5, 4, 6]

# number.sort(reverse=True)
# result = 0
# count = 0
#
# plus_count = 0
#
# while plus_count < M:
#     if count < K:
#         result += number[0]
#         count += 1
#     else:
#         result += number[1]
#         count = 0
#
#     plus_count += 1
#
# print(result)

number.sort()
first = number[n - 1]
second = number[n - 2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)


n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += (count) * first
result += (m - count) * second

print(result)