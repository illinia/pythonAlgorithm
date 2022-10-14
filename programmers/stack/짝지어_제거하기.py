s = "baabaa"
# s = "cdcd"

stack = []
s = list(s)
stack.append(s.pop())

while s:
    p = s.pop()
    if not stack:
        stack.append(p)
        continue

    sp = stack.pop()

    if sp == p:
        continue
    else:
        stack.append(sp)
        stack.append(p)


# print(1 if len(stack) == 0 else 0)