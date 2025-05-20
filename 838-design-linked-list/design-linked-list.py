class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left        

    def get(self, index: int) -> int:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        if cur and cur != self.right and index == 0:
            return cur.data
        return -1

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.left.next
        self.left.next.prev = new_node
        self.left.next = new_node
        new_node.prev = self.left


    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.right
        new_node.prev = self.right.prev
        self.right.prev.next = new_node
        self.right.prev = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        if cur and index == 0:
            new_node = ListNode(val)
            new_node.next = cur
            new_node.prev = cur.prev
            cur.prev.next = new_node
            cur.prev = new_node

    def deleteAtIndex(self, index: int) -> None:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        
        if cur and cur != self.right and index == 0:
            prev = cur.prev
            nxt = cur.next
            prev.next = cur.next
            nxt.prev = cur.prev
        

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)