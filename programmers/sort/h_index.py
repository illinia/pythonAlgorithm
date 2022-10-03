citations = [3, 0, 6, 1, 5]

citations.sort(reverse=True)

print(list(enumerate(citations)))

for i, c in enumerate(citations):
    if i >= c:
        print(i)

        max(max(x) for x in citations)