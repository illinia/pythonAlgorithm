def lifo(input):
    stack = list()

    for s in input:
        if s == '(':
            stack.append(')')
        elif s == '{':
            stack.append('}')
        elif s == '[':
            stack.append(']')
        elif (len(stack) == 0) or (s != stack.pop()):
            return False
    return True



input1 = ")("
input2 = '([]}'
input3 = '{()[]}'

assert lifo(input1) is False
assert lifo(input2) is False
assert lifo(input3) is True