import math


def is_prime_number(x):
    # for i in range(2, x):
    #     if x % i == 0:
    #         return False
    # return True
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


print(is_prime_number(4))
print(is_prime_number(7))

n = 1000
array = [True for i in range(n + 1)]

for i in range(2, int(math.sqrt(n)) + 1):
    if array[i] == True:
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1

for i in range(2, n + 1):
    if array[i]:
        print(i, end=' ')

print()


# 투포인터
n = 5
m = 5
data = [1,2,3,2,5]

count = 0
interval_sum = 0
end = 0

for start in range(n):
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1
    if interval_sum == m:
        count += 1
    interval_sum -= data[start]

print(count)

n, m = 3, 4
a = [1,3,5]
b = [2,4,6,8]

result = [0] * (n + m)
i = 0
j = 0
k = 0

while i < n or j < m:
    if j >= m or (i < n and a[i] <= b[j]):
        result[k] = a[i]
        i += 1
    else:
        result[k] = b[j]
        j += 1
    k += 1

for i in result:
    print(i, end=' ')

print()


# 구간합
n = 5
data = [10, 20, 30, 40, 50]

sum_value = 0
prefix_sum = [0]
for i in data:
    sum_value += i
    prefix_sum.append(sum_value)

left = 3
right = 4
print(prefix_sum[right] - prefix_sum[left - 1])

# 순열
import itertools

data = [1, 2]

for x in itertools.permutations(data, 2):
    print(list(x))

data = [1,2,3]

for x in itertools.combinations(data, 2):
    print(list(x), end=' ')
print()

# 소수구하기
# import math
#
# m, n = map(int, input().split())
# array = [True for i in range(1000001)]
# array[1] = 0
#
# for i in range(2, int(math.sqrt(n)) + 1):
#     if array[i]:
#         j = 2
#         while i * j <= n:
#             array[i * j] = False
#             j += 1
#
# for i in range(m, n + 1):
#     if array[i]:
#         print(i)

# 암호 만들기
from itertools import combinations

vowels = ('a', 'e', 'i', 'o', 'u')
l, c = map(int, input().split())

array = input().split(' ')
array.sort()

for password in combinations(array, l):
    count = 0
    for i in password:
        if i in vowels:
            count += 1

    if count >= 1 and count <= l - 2:
        print(''.join(password))