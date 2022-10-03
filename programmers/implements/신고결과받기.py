id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2


report_count = {}
report_list = {}

for i in id_list:
    report_count[i] = 0
    report_list[i] = []

for r in report:
    a, b = r.split(' ')

    report_count[b] += 1
    report_list[b].append(a)


new_list = list(filter(lambda x: report_count[x] >= k, report_count))

answer = [0] * len(id_list)

for i in new_list:
    for j in report_list[i]:
        answer[id_list.index(j)] += 1

print(answer)