# n, t, m, p = 2, 4, 2, 1
# n, t, m, p = 16, 16, 2, 1
n, t, m, p = 16, 16, 2, 2

new = ''
i = 0

while True:
    a = ''
    number = i
    while True:
        print(number, n)
        number, mod = divmod(number, n)
        print(number, mod)

        if mod == 10:
            mod = 'A'
        elif mod == 11:
            mod = 'B'
        elif mod == 12:
            mod = 'C'
        elif mod == 13:
            mod = 'D'
        elif mod == 14:
            mod = 'E'
        elif mod == 15:
            mod = 'F'
        a += str(mod)

        if number == 0:
            break
    a = a[::-1]
    new += a
    i += 1

    if len(new) > (t * m):
        break

n_list = []

print(new)

while new:
    if len(new) >= m:
        new_word = new[:m]
        n_list.append(new_word)
        new = new[m:]
    else:
        n_list.append(new)
        new = ''

answer = ''

print(n_list)

for i in n_list:
    if len(i) > len(i):
        answer += i[p]

n_list = n_list[:t]

answer = str(''.join(list(map(lambda x: x[p - 1], n_list))))
print(answer)