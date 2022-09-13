import sys

n, k = map(int, input().split())

# n이 100억 이상의 큰수일 경우 시간초과
# count = 0
#
# while n >= k:
#     if n % k != 0:
#         n -= 1
#     else:
#         n //= k
#     count += 1
#
# while n > 1:
#     n -= 1
#     count += 1
#
# print(count)

result = 0

while True:
    target = (n // k) * k
    result += (n - target)
    n = target

    if n < k:
        break
    result += 1
    n //= k

result += (n - 1)
print(result)