numbers = [2, 7]
answer = []

for i in numbers:
    if i % 2 == 0:
        answer += i + 1
    else:
        n = '0' + bin(i)[2:]
        index = n.rfind('0')
        n = list(n)
        n[index] = '1'
        n[index + 1] = '0'
        answer.append(int(''.join(n), 2))

print(answer)
