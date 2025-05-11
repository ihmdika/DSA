class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = Node()
        self.tail = self.head

    def length(self):
        cur = self.head.next
        total = 0
        while cur:
            total += 1
            cur = cur.next
        return total 

    def get(self, index: int) -> int:
        if index < 0 or index >= self.length():
            return -1

        cur = self.head.next
        step = 0
        while True:
            if step == index:
                return cur.data
            cur = cur.next
            step += 1
        
    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if not new_node.next: 
            self.tail = new_node

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        self.tail.next = new_node
        self.tail = self.tail.next

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.length():
            return None
        if index == self.length():
            self.addAtTail(val)
            return None
        else:
            new_node = Node(val)
            cur = self.head # 'dummy head'
            i = 0 
            while cur:
                if i == index:
                    new_node.next = cur.next
                    cur.next = new_node
                    return None
                i += 1
                cur = cur.next


    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length():
            return None
        
        cur = self.head
        i = 0
        while cur:
            if i == index:
                to_delete = cur.next
                cur.next = to_delete.next
                if to_delete == self.tail:
                    self.tail = cur
                return
            cur = cur.next
            i += 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)