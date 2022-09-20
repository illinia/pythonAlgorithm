# s = list(map(int, input()))
#
# zero = 0
# one = 0
#
# if s[0] == 1:
#     one += 1
# else:
#     zero += 1
#
# for i in range(len(s) - 1):
#     if s[i] != s[i + 1]:
#         if i == 0:
#             zero += 1
#         else:
#             one += 1
#
#
# print(zero, one)

data = input()
count0 = 0
count1 = 0

if data[0] == '1':
    count0 += 1
else:
    count1 += 1

for i in range(len(data) - 1):
    if data[i] != data[i + 1]:
        if data[i + 1] == '1':
            count0 += 1
        else:
            count1 += 1

print(count0, count1)

# 0001100