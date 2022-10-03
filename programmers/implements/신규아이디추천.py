new_id = "...!@BaT#*..y.abcdefghijklm"

new_id = new_id.lower()

new = ''
for n in new_id:
    if n.islower() or n.isdigit() or n == '-' or n == '_' or n == '.':
        new += n
new_id = new

while True:
    if new_id.find("..") != -1:
        new_id = new_id.replace("..", ".", 1)
    else:
        break

new_id = new_id.strip(".")

if len(new_id) == 0:
    new_id = "a"

if len(new_id) >= 16:
    new_id = new_id[0:15]

new_id = new_id.rstrip(".")

while len(new_id) <= 2:
    new_id += new_id[-1]

print(new_id)