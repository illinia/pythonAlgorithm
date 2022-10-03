# dartResult = "1S2D*3T"
# dartResult = "1D2S#10S"
dartResult = "1D2S0T"

data = [[] for _ in range(len(dartResult) + 1)]

answer = 0

i = 0

for index, d in enumerate(dartResult):
    if d.isdigit() and dartResult[index + 1].isdigit():
        continue
    elif d.isdigit() and dartResult[index - 1].isdigit():
        i += 1
        data[i].append(int(dartResult[index - 1]+d))
    elif d.isdigit():
        i += 1
        data[i].append(int(d))
    elif d == 'S':
        data[i].append('S')
    elif d == 'D':
        data[i].append('D')
    elif d == 'T':
        data[i].append('T')
    elif d == '*':
        data[i].append('*')
        data[i - 1].append('*')
    elif d == '#':
        data[i].append('#')
    print(data)
    print(i)

for d in data:
    result = 0
    if len(d) > 0:
        for i in d:
            if str(i).isdigit():
                result += i
            elif i == 'S':
                result **= 1
            elif i == 'D':
                result **= 2
            elif i == 'T':
                result **= 3
            elif i == '*':
                result *= 2
            elif i == '#':
                result *= -1
    answer += result

print(answer)