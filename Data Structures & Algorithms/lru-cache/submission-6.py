class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = None
        self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity    
        self.right = Node(0,0)
        self.left = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def removeLRU(self):
        self.left.next = self.left.next.next
        self.left.next.prev = self.left

    def unlink(self,key):
        self.cache[key].prev.next = self.cache[key].next
        self.cache[key].next.prev = self.cache[key].prev

    def makeMostRecent(self,key):
        self.right.prev.next = self.cache[key]
        self.cache[key].prev = self.right.prev
        self.cache[key].next = self.right
        self.right.prev = self.cache[key]

    def get(self, key: int) -> int:
        if key in self.cache:
            self.unlink(key)
            self.makeMostRecent(key)
         #   self.left.print_list(self.left)
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self.unlink(key)

        else:
            self.cache[key] = Node(key,value)
        self.makeMostRecent(key)
       # self.left.print_list(self.left)
        if len(self.cache) > self.cap:
            lru = self.left.next.key
            self.unlink(lru)
            del self.cache[lru]
            #self.left.print_list(self.left)
    
