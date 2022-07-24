# 정렬
import sys

N = int(sys.stdin.readline())

words = []

for _ in range(N):
    words.append(sys.stdin.readline().rstrip())

words = set(words)

words = list(words)

words.sort()
words.sort(key=len)

for i in words:
    print(i)