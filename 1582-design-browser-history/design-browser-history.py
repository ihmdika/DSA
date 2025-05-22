class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.current = Node(homepage)

    def visit(self, url: str) -> None:
        new_node = Node(url)
        new_node.prev = self.current
        self.current.next = new_node
        self.current = new_node

    def back(self, steps: int) -> str:
    
        while self.current.prev and steps > 0:
            self.current = self.current.prev
            steps -= 1
    
        return self.current.data

    def forward(self, steps: int) -> str:
        while self.current.next and steps > 0:
            self.current = self.current.next
            steps -= 1

        return self.current.data    


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)