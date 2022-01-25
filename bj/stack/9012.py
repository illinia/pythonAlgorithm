n = int(input())

lines = []

for _ in range(n):
    lines.append(list(input()))

for line in lines:
    stack = []
    for i in range(len(line)):
        if len(stack) == 0:
            stack.append(line[i])
        elif line[i] == ')' and stack[-1] == '(':
            stack.pop()
        else:
            stack.append(line[i])

    if len(stack) == 0:
        print('YES')
    else:
        print('NO')