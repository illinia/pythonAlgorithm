n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1

for i in data:
    if target < i:
        break
    else:
        target += i

print(target)

# 5
# 3 2 1 1 9