class Node(object):
    def __init__(self, url, next=None, prev=None):
        self.url = url
        self.next = next
        self.prev = prev


class BrowserHistory(object):
    def __init__(self, url):
        self.current = Node(url=url)

    def visit(self, url):
        # new_node 를 current.next 로 저장
        # current 에서 next 이후 노드들은 다 삭제
        new_node = Node(url)
        self.current.next = new_node
        new_node.prev = self.current
        self.current = self.current.next

    def back(self, steps):
        # steps 수 만큼 뒤로가기 -> current 를 steps 수 만큼 옮긴다.
        # steps 를 1씩 줄여가며 current 의 prev 를 current 에 저장
        # steps 수 보다 이전 노드의 갯수가 적으면 반복문 탈출 -> current.prev == None
        while steps > 0 and self.current.prev is not None:
            steps -= 1
            self.current = self.current.prev
        url = self.current.url
        print(url)
        return url

    def forward(self, steps):
        while steps > 0 and self.current.next is not None:
            steps -= 1
            self.current = self.current.next
        url = self.current.url
        print(url)
        return url


browserHistory = BrowserHistory("leetcode.com")
browserHistory.visit("google.com")
browserHistory.visit('facebook.com')
browserHistory.visit('youtube.com')
assert browserHistory.back(1) == 'facebook.com', 'wrong'

assert browserHistory.back(1) == 'google.com', 'wrong'

assert browserHistory.forward(1) == 'facebook.com', 'wrong'

browserHistory.visit('linkedin.com')
assert browserHistory.forward(2) == 'linkedin.com', 'wrong'
assert browserHistory.back(2) == 'google.com', 'wrong'
assert browserHistory.back(7) == 'leetcode.com', 'wrong'