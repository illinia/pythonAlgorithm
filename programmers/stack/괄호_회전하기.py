s = "[](){}"
# s = "}]()[{"

d = {'{': '}', '[': ']', '(': ')'}
count = 0

s = list(s)

for i in range(len(s)):
    stack = []
    ns = s.copy()
    ns = ns[i:] + ns[:i]

    stack.append(ns.pop())

    while ns:
        last = ns.pop()

        if last in d and stack and d[last] == stack[-1]:
            stack.pop()
        else:
            stack.append(last)

    if not stack:
        count += 1

print(count)