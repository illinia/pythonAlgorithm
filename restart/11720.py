import sys

N = int(sys.stdin.readline().strip())

number = sys.stdin.readline().strip()

sum_number = 0

for i in str(number):
    sum_number += int(i)

print(sum_number)