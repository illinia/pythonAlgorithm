money = [1,2,3,1]

d = [0] * len(money)
d[0] = money[0]
d[1] = money[1]

for i in range(2, len(money)):
    d[i] =\
        max(d[i - 2]
            + money[i],
            d[i - 1])

answer = d[-1]

print(answer)