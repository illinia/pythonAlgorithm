import sys

n = int(sys.stdin.readline())

stack = []
result = []
count = 0

success = True

for i in range(n):
    number = int(sys.stdin.readline())

    while count < number:
        count += 1
        stack.append(count)
        result.append('+')

    if stack[-1] == number:
        stack.pop()
        result.append('-')
    else:
        success = False

if success:
    print('\n'.join(result))
else:
    print('NO')
