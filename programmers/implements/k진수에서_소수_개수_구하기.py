n = 437674
k = 3
# n = 110011
# k = 10

n_copy = n
a = ''

while n_copy > 0:
    n_copy, mod = divmod(n_copy, k)
    a += str(mod)

a = a[::-1]
a = a.split('0')
if '' in a:
    a.remove('')

a_list = list(map(int, a))

print(a_list)

max_p = max(a_list)

p_list = [True for _ in range(n + 1)]
p_list[0] = False
p_list[1] = False

for i in range(2, max_p + 1):
    if p_list[i] == True:
        for j in range(i + i, max_p + 1, i):
            p_list[j] = False

count = 0

for i in a_list:
    if p_list[i] == True:
        count += 1

print(count)
