import sys

# 2 <= n <= 1,000
# 1 <= m <= 10,000
# 1 <= k <= 10,000

n, m, k = map(int, sys.stdin.readline().split())

numbers = list(map(int, sys.stdin.readline().split()))

# max1 = max(numbers)
# numbers.remove(max1)
# max2 = max(numbers)

numbers.sort()
max1 = numbers[n - 1]
max2 = numbers[n - 2]

# m의 크기가 100억 이상으로 커지면 시간초과 판정
#
# result = 0
#
# while True:
#     # if m > 3:
#     #     result += max1 * 3 + max2
#     #     m -= 4
#     # else:
#     #     result += max1 * m
#     #     m = 0
#     for i in range(k):
#         if m == 0:
#             break
#         result += max1
#         m -= 1
#     if m == 0:
#         break
#     result += max2
#     m -= 1

count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += (count) * max1
result += (m - count) * max2

print(result)

# 5 8 3
# 2 4 5 4 6