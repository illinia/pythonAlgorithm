# 리스트 컴프리헨션
array = [i for i in range(20) if i % 2 == 1]

print(array)

array = [i * i for i in range(1, 10)]

print(array)

n = 3
m = 4
array = [[0] * m for _ in range(n)]

print(array)

a = [1, 4, 3]
print("기본 리스트: ", a)

a.append(2)
print("삽입: ", a)

a.sort()
print("오름차순 정렬: ", a)

a.sort(reverse=True)
print("내림차순 정렬: ", a)

a.reverse()
print("원소 뒤집기: ", a)

a.insert(2, 3)
print("인덱스 2에 3 추가: ", a)

print("값이 3인 데이터 개수: ", a.count(3))

a.remove(1)
print("값이 1인 데이터 삭제: ", a)

a = [1,2,3,4,5,5,5]
remove_set = {3, 5}

result = [i for i in a if i not in remove_set]
print(result)

# 문자열 초기화
data = 'Hello World'
print(data)

data = "Don't you know \"Python\"?"
print(data)

a = "Hello"
b = "World"

print(a + " " + b)

a = "String"
print(a * 3)

a = "ABCDEF"
print(a[2:4])

a = (1,2,3,4)
print(a)

# 사전자료형

data = dict()
data['사과'] = "Apple"
data["바나나"] = "Banana"
data["코코넛"] = "Coconut"

print(data)

if "사과" in data:
    print("'사과'를 키로 가지는 데이터가 존재합니다.")

key_list = data.keys()
value_list = data.values()
print(key_list)
print(value_list)

for key in key_list:
    print(data[key])

# 집합 자료형
data = set([1,1,2,3,4,4,5])
print(data)

data = {1,1,2,3,4,4,5}
print(data)

a = set([1,2,3,4,5])
b = set([3,4,5,6,7])

print(a | b)
print(a & b)
print(a - b)

# 조건문
a = [1,2,3,4,5,5,5]
remove_set = {3, 5}

result = [i for i in a if i not in remove_set]
print(result)

# 반복문 while
i = 1
result = 0
while i < 9:
    if i % 2 == 1:
        result += i
    i += 1

print(result)

# for
result = 0

for i in range(1, 10):
    result += i

print(result)

scores = [90, 85, 77, 65, 97]

for i in range(len(scores)):
    if scores[i] >= 80:
        print(i + 1, "번 학생은 합격입니다.")

cheating_list = {2, 4}

for i in range(5):
    if i + 1 in cheating_list:
        continue
    if scores[i] >= 80:
        print(i + 1, "번 학생은 합격입니다.")

for i in range(2, 10):
    for j in range(1, 10):
        print(i, "X", j, "=", i * j)
    print()


# 함수
def add(a, b):
    return a + b


print(add(3, 7))

print((lambda a, b: a + b)(3, 7))

# 입출력
# 5
# 65 90 75 34 99
# n = int(input())
#
# data = list(map(int, input().split()))
#
# data.sort(reverse=True)
# print(data)

# n, m, k = map(int, input().split())
# print(n, m, k)

answer = 7
print("정답은 " + str(answer) + "입니다")
print("정답은 ", answer, "입니다.")
print(f"정답은 {answer}입니다.")

# 내장함수
result = sum([1,2,3,4,5])
print(result)

result = min(7, 3, 5, 2)
print(result)

result = max(7, 3, 5, 2)
print(result)

result = eval("(3+5) * 7")
print(result)

result = sorted([9, 1, 8, 5, 4])
print(result)
result = sorted(result, reverse=True)
print(result)

result = sorted([("홍길동", 35), ("이순신", 75), ("아무개", 50)], key = lambda x: x[1], reverse=True)
print(result)

from itertools import permutations, combinations, product, combinations_with_replacement

data = ["A", "B", "C"]
result = list(permutations(data, 3))
print(result)

result = list(combinations(data, 2))
print(result)

data = ["A", "B", "C"]
result = list(product(data, repeat=2))
print(result)

result = list(combinations_with_replacement(data, 2))
print(result)

import heapq

def heapsort(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, value)
    for _ in range(len(h)):
        result.append(heapq.heappop(h))
    return result


result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)


def heapsortmax(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, -value)
    for _ in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result = heapsortmax([1,3,5,7,9,2,4,6,8,0])
print(result)

from bisect import bisect_left, bisect_right

a = [1,2,4,4,8]
x = 4

print(bisect_left(a, x))
print(bisect_right(a, x))

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index


a = [1,2,3,3,3,3,4,4,8,9]

print(count_by_range(a, 4, 4))
print(count_by_range(a, -1, 3))

from collections import deque

data = deque([2,3,4])
data.appendleft(1)
data.append(5)

print(data)
print(list(data))

from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue'])
print(counter['green'])
print(dict(counter))

import math
print(math.factorial(5))

print(math.sqrt(7))

print(math.gcd(21, 14))

print(math.pi)
print(math.e)