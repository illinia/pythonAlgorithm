n = 3
words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]

words = list(reversed(words))
last_words = []
answer = [0, 0]
last = ''
turn = 1

while words:
    w = words.pop()

    if (last == w[0] and w not in last_words) or last == '':
        last = w[-1]
        last_words.append(w)
    else:
        a = len(last_words) & n if len(last_words) & n != 0 else n
        answer = [a, turn]
        break

    if len(last_words) % n == 0:
        turn += 1

# return answer
print(3 % 3)