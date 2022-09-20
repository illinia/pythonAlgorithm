s = list(map(int, input()))

s.sort()

result = s[0]

for i in range(1, len(s)):
    num = int(s[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num
    # if number == 0:
    #     continue
    # else:
    #     if result == 0:
    #         result += number
    #     else:
    #         result *= number

print(result)

# 02984
# 567