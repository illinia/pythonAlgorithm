# msg = 'KAKAO'
msg = 'TOBEORNOTTOBEORTOBEORNOT'
d = {}

w = ord('A')
index = 1

while True:
    d[chr(w)] = index

    w = ord(chr(w + 1))

    if not chr(w).isalpha():
        break
    else:
        index += 1

answer = []

msg = list(msg)

while msg:
    for i in range(len(msg), 0, -1):
        # print(d)

        w = ''.join(msg[0:i])
        print(w, msg, i, d)

        if w in d:
            answer.append(d[w])

            if i < len(msg) - 1:
                new_word = w + msg[i]
                # print(w, new_word)
                index += 1
                d[new_word] = index

            msg = msg[i:]
            break

print(answer)