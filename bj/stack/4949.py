

while True:
    sentence = input()

    if sentence == '.':
        break

    sentence = list(sentence.replace(' ', ''))
    stack = []
    words = ['(', ')', '[', ']']

    for i in sentence:
        if i in words:
            if (len(stack) != 0 and i == ')' and stack[-1] == '(') or (len(stack) != 0 and i == ']' and stack[-1] == '['):
                stack.pop()
            else:
                stack.append(i)

    if len(stack) != 0:
        print('no')
    else:
        print('yes')