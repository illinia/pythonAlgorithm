# clothes = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]

h = {}
for clothe, type in clothes:
    h[type] = h.get(type, 0) + 1

print(h)

result = 1

for type in h:
    result *= (h[type] + 1)

print(result - 1)