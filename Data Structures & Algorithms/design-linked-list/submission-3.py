class ListNode():
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None
        

class MyLinkedList:

    def __init__(self):
        self.dummy = ListNode(0)
        self.last = None        
        self.length = 0

    def get(self, index: int) -> int:
        current = self.dummy.next
        while current and index > 0:
            current = current.next
            index -= 1
        if not current:
            return -1
        else:
            return current.val
        
    def addAtHead(self, val: int) -> None:
        newNode = ListNode(val)
        self.length += 1
        if self.dummy.next is None:
            self.dummy.next = newNode
            newNode.prev = self.dummy
            self.last = newNode
            return
        save = self.dummy.next
        save.prev = newNode
        self.dummy.next = newNode
        newNode.prev = self.dummy
        newNode.next = save



    def addAtTail(self, val: int) -> None:
        newNode = ListNode(val)
        self.length += 1
        if self.last is None:
            self.dummy.next = newNode
            newNode.prev = self.dummy
            self.last = newNode
            return
        self.last.next = newNode
        newNode.prev = self.last
        self.last = newNode
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            return
        elif index == self.length:
            self.addAtTail(val)
        elif index == 0:
            self.addAtHead(val)
        else:
            newNode = ListNode(val)
            current = self.dummy
            for i in range(index):
                current = current.next
            save = current.next
            current.next = newNode
            newNode.prev = current
            newNode.next = save
            save.prev = newNode
            self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length:
            return 
        elif index == self.length - 1:
            save = self.last.prev
            save.next = None
            self.last.prev = None
            self.last = save
        elif index == 0:
            save = self.dummy.next.next
            save.prev = self.dummy
            self.dummy.next = save
        else:
            current = self.dummy.next
            for i in range(index):
                current = current.next
            before = current.prev
            after = current.next
            current.prev = None
            current.next = None
            before.next = after
            after.prev = before
        self.length -= 1



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)