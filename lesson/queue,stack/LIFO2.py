def calculateTemperature(temperatures):
    stack = list()
    answer = [0] * len(temperatures)

    for (index, t) in enumerate(temperatures):
        if not stack:
            stack.append((index, t))
        else:
            # 스택 top 요소가 현재 온도보다 낮으면
            # 스택 top 요소 pop 해주고, 스택 top 온도가 해당 온도보다 같거나 낮을 때 까지 계속 반복
            while stack and stack[-1][1] < t:
                # 스택 top 요소 pop (해당 인덱스 = 날짜, 온도)
                # 필요한 것은 날짜이므로 날짜만 사용
                prev_date, _ = stack.pop()
                # 답 배열에 넣을 걸린 날 계산
                answer_date = index - prev_date
                # 답 배열에 해당 날짜에 해당하는 위치에 걸린 날 넣기
                answer[prev_date] = answer_date
            # 스택 pop 종료이거나 애초에 반복문 실행이 안되었다면(top 온도보다 해당 온도가 낮거나 같을 때)
            # 스택에 해당 온도 push
            stack.append((index, t))
    return answer







input1 = [73, 74, 75, 71, 69, 72, 76, 73]
answer1 = [1,1,4,2,1,1,0,0]
input2 = [30, 40, 50, 60]
answer2 = [1,1,1,0]
input3 = [30, 60, 90]
answer3 = [1,1,0]

assert calculateTemperature(input1) == answer1
assert calculateTemperature(input2) == answer2
assert calculateTemperature(input3) == answer3