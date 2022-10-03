s = "   test   "

answer = ''

for i, a in enumerate(s):
    if (i == 0 and a.isalpha()) or (i != 0 and s[i - 1] == ' ' and a.isalpha()):
        answer += a.upper()
    elif a.isalpha():
        answer += a.lower()
    else:
        answer += a

print(answer)