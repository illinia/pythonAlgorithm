import math

fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN",
           "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

def calculate_fee(total_time, basic_time, basic_fee, basic_time_unit, basic_fee_unit):
    if total_time <= basic_time:
        return basic_fee
    else:
        return basic_fee + math.ceil((total_time - basic_time) / basic_time_unit) * basic_fee_unit


basic_time, basic_fee, basic_time_unit, basic_fee_unit = fees[0], fees[1], fees[2], fees[3]
max_time = 23 * 60 + 59

r = []

pay = {}

for i in records:
    a = i.split(' ')
    time, number, status = a[0], a[1], a[2]

    if number not in pay:
        pay[number] = 0

    h, m = list(map(int, time.split(":")))

    time = (h * 60) + m

    r.append((time, number, status))

temp = {}

for i in r:
    if i[2] == 'IN':
        temp[i[1]] = i[0]
    else:
        in_time = temp[i[1]]
        del temp[i[1]]
        total_time = i[0] - in_time
        pay[i[1]] += total_time

for t in temp:
    number, time = t, temp[t]

    total_time = max_time - time

    pay[number] += total_time

answer = {}

print(pay)

for i in pay:
    answer[i] = calculate_fee(pay[i], basic_time, basic_fee, basic_time_unit, basic_fee_unit)

answer = sorted(answer.items())

print(list(map(lambda x: x[1], answer)))
