board = [
    [0,0,0,0,0],
    [0,0,1,0,3],
    [0,2,5,0,1],
    [4,2,4,4,2],
    [3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

picked = []
answer = 0

for move in moves:
    for b in board:
        p = b[move - 1]
        if p != 0:
            if len(picked) > 0 and picked[-1] == p:
                picked.pop()
                answer += 2
            else:
                picked.append(p)
            b[move - 1] = 0
            break


print(answer)
