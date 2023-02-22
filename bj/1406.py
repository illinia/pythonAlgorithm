"""
1. 문제 이해
    1. 설명
        * 한 줄로 된 에디터 구현, 최대 600,000 글자 입력 가능
        * 커서 존재, 문장의 맨 앞, 맨 뒤, 중간 임의의 곳에 위치할 수 있다.
        * L: 커서를 왼쪽으로 한 칸 옮김(맨 앞이면 무시)
          D: 오른쪽으로 한 칸 옮김(맨 뒤이면 무시)
          B: 왼쪽에 있는 문자를 삭제(맨 앞이면 무시)
          P: 문자를 커서 왼쪽에 추가
    2. 제약 사항
        1. 편집기에 입력되어 있는 문자열 주어짐
           길이 N, 영어 소문자, 0 <= N <= 100,000
        2. 입력할 명령어의 개수 M, 1 <= M <= 500,000
        3. 셋째 줄부터 M 개의 줄에 입력할 명령어가 주어짐
        4. 시간 제한이 0.3 초 이므로 30,000,000 까지 가능
2. 접근 방법
    * 문자열이 100,000 길이까지 존재할 수 있다.
    * 입력할 명령어의 개수는 반복문으로 해결해야 하므로 시간복잡도에 영향이 있다.
      시간 제한이 있으므로 O(N) 까지 해결 가능
    * 입력 명령어 개수에서 O(N)을 사용하고 각 명령어에서 O(1)으로 해결할 수 있는 방법을 찾아야 한다.
    * 커서가 존재하므로 명령어로 행할 수 있는 범위는 각 요소의 앞, 뒤, 자신에만 한정된다.
      삽입, 삭제시 O(1) 시간이 필요하므로 연결 리스트로 구현하면 될 듯 싶다.
    * 연결 리스트로 구현시 필요한 요구사항
        1. 앞, 뒤로 커서를 이동(가리기는 요소의 주소값을 저장할 수 있는 변수)
        2. 삭제
        3. 추가
    * 연결 리스트 노드 요구사항
        1. 각 노드에는 값이 있다.
        2. 앞, 뒤로 이동할 수 있는 주소 값이 필요하다.
        3. 커서가 마지막 글자 오른쪽에도 위치할 수 있으므로 마지막은 항상 None 을 value 로 갖는 노드로 지정
3. 코드 설계
    1. 연결 리스트 노드
        1. 값(필수)
        2. 앞, 뒤 노드 주소값(기본 값 None)
    2. 연결 리스트
        0. 생성자
            1. 현재 노드에 None 저장
            2. 머리 노드에 None 저장
        1. 커서 왼쪽 이동
            1. 현재 노드의 prev 노드가 없으면 리턴
            2. 있으면 현재 노드 = 현재 노드의 prev 노드
        2. 커서 오른쪽 이동
            1. 현재 노드의 next 노드가 없으면 리턴
            2. 있으면 현재 노드 = 현재 노드의 next 노드
        3. 커서 왼쪽 문자 삭제
            1. 현재 노드가 머리 노드이면
                1. 삭제할 문자가 없으므로 리턴
            2. 현재 노드의 prev 가 머리 노드이면
                1. 현재 노드의 prev = None
                2. 머리 노드 = 현재 노드
            3. 이외의 경우
                1. prev = 현재 노드의 prev 의 prev
                2. prev 의 next = 현재 노드
                3. 현재 노드의 prev = prev
        4. 커서 왼쪽 문자 추가
            1. 현재 노드가 머리 노드이면
                1. 새로운 문자의 노드 저장
                2. 머리 노드 = 새로운 노드
                3. 현재 노드의 prev = 새로운 노드
                4. 새로운 노드의 next = 현재 노드
            2. 아니면
                1. 새로운 문자의 노드 저장, 현재 노드의 prev 노드 저장
                2. prev 노드의 next = 새로운 노드
                3. 새로운 노드의 prev = prev 노드
                4. 현재 노드의 prev = 새로운 노드
                5. 새로운 노드의 next = 현재 노드
        5. 현재 노드의 오른쪽에 문자 추가(문자열 입력용)
            1. 새로운 노드 생성
            2-1. 현재 노드가 없으면(연결 리스트 생성 직후)
                 현재 노드 = 새로운 노드, 머리 노드 = 새로운 노드, 리턴
            2. 현재 노드의 next = 새로운 노드
            3. 새로운 노드의 prev = 현재 노드
            4. 현재 노드를 새로운 노드로 저장
    3. 문자열 입력, 연결 리스트 생성, 입력된 문자열을 반복문 돌면서 연결 리스트에 저장
    4. M 입력
    5. M 만큼 반복문 돌면서 입력
        1. 입력된 값의 첫 번째 값으로 어떤 명령인지 확인
        2. 해당 명령에 따른 연결 리스트 명령 실행
    6. 현재 노드 = 연결 리스트 머리 노드
    7. 결과 문자열에 현재 노드값 더하기
    8. 반복문 순회
        1. 연결 리스트 다음 노드가 None 이면 반복문 종료
        2. 현재 노드 = 다음 노드
        3. 결과 문자열에 현재 노드값 더하기

"""

# # 연결 리스트 풀이(시간 초과)
# from sys import stdin
#
#
# # 1
# class Node(object):
#     def __init__(self, value, prev=None, next=None):
#         # 1-1
#         self.value = value
#         # 1-2
#         self.prev = prev
#         self.next = next
#
#
# class LinkedList(object):
#     # 0
#     def __init__(self):
#         # 0-1
#         self.current = None
#         self.head = None
#
#     # 1
#     # 커서 왼쪽으로 옮김, 커서는 문자열 제일 오른쪽에 value 가 None 인 노드가 될 수 있음
#     def command_l(self):
#         # 1-1
#         if self.current.prev is None:
#             return
#         # 1-2
#         self.current = self.current.prev
#
#     # 2
#     # 커서 오른쪽으로 옮김
#     def command_d(self):
#         # 2-1
#         if self.current.next is None:
#             return
#         # 2-2
#         self.current = self.current.next
#
#     # 3
#     # 왼쪽 문자 삭제
#     def command_b(self):
#         # 3-1
#         if self.current == self.head:
#             return
#         # 3-2
#         elif self.current.prev == self.head:
#             # 3-2-1
#             self.current.prev = None
#             # 3-2-2
#             self.head = self.current
#         # 3-3
#         else:
#             # 3-3-1
#             prev_node = self.current.prev.prev
#             # 3-3-2
#             prev_node.next = self.current
#             # 3-3-3
#             self.current.prev = prev_node
#
#     # 4
#     # 왼쪽에 문자 추가
#     def command_p(self, value):
#         # 4-1
#         if self.current == self.head:
#             # 4-1-1
#             new_node = Node(value)
#             # 4-1-2
#             self.head = new_node
#             # 4-1-3
#             self.current.prev = new_node
#             # 4-1-4
#             new_node.next = self.current
#         # 4-2
#         else:
#             # 4-2-1
#             new_node = Node(value)
#             prev_node = self.current.prev
#             # 4-2-2
#             prev_node.next = new_node
#             # 4-3-3
#             new_node.prev = prev_node
#             # 4-3-4
#             self.current.prev = new_node
#             # 4-3-5
#             new_node.next = self.current
#
#     # 5
#     # 현재 노드의 오른쪽에 문자 추가(문자열 입력용)
#     def command_append(self, value):
#         # 5-1
#         new_node = Node(value)
#         # 5-2-1
#         if self.current is None:
#             self.current = new_node
#             self.head = new_node
#             return
#         # 5-2
#         self.current.next = new_node
#         # 5-3
#         new_node.prev = self.current
#         # 5-4
#         self.current = new_node
#
#
# # 3 문자열 입력, 연결 리스트 생성, 입력된 문자열을 반복문 돌면서 연결 리스트에 저장
# words = stdin.readline()
# linked_list = LinkedList()
# for w in words:
#     linked_list.command_append(w)
#
# # 4 M 입력
# M = int(stdin.readline())
#
# # 5 M 만큼 반복문 돌면서 입력
# for _ in range(M):
#     # 5-1
#     command = list(map(str, stdin.readline().split()))
#
#     first_word = command[0]
#
#     if first_word == 'L':
#         linked_list.command_l()
#     elif first_word == 'D':
#         linked_list.command_d()
#     elif first_word == 'B':
#         linked_list.command_b()
#     else:
#         linked_list.command_p(command[1])
#
# linked_list.current = linked_list.head
# result = linked_list.current.value
#
# while linked_list.current.next is not None:
#     linked_list.current = linked_list.current.next
#     result += linked_list.current.value
#
# print(result)



# 스택 두개 사용해서 풀이

from sys import stdin

stack1 = list(stdin.readline().rstrip())
stack2 = list()
M = int(stdin.readline())

for _ in range(M):
    command = list(map(str, stdin.readline().split()))

    if command[0] == 'L':
        if stack1:
            stack2.append(stack1.pop())
    elif command[0] == 'D':
        if stack2:
            stack1.append(stack2.pop())
    elif command[0] == 'B':
        if stack1:
            stack1.pop()
    else:
        stack1.append(command[1])

# 리스트의 reserve 함수 사용시 빈 리스트인 경우 TypeError 가 던져진다.
stack1.extend(reversed(stack2))

print(''.join(stack1))









