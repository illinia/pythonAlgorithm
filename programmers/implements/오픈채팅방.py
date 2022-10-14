record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

l = []

for r in record:
    print(r.split(' '))
    s = r.split(' ')
    l.append(s)

print(l)