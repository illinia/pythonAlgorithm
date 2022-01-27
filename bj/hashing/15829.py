n = int(input())

strings = list(input())

result = 0
M = 1234567891

for i in range(len(strings)):
    result += ((ord(strings[i]) - 96) * (31 ** i))

print(result % M)