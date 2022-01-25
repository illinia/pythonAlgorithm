n = int(input())

length = list(map(int, input().split()))
stations = list(map(int, input().split()))

minValue = stations[0]
result = 0

for i in range(n - 1):
    if stations[i] < minValue:
        minValue = stations[i]
    result += minValue * length[i]

print(result)
