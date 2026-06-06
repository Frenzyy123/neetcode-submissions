class MinStack:

    def __init__(self):
        self.stack = []
        self.MinStack = []
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.MinStack or val <= self.MinStack[-1]:
            self.MinStack.append(val)

    def pop(self) -> None:
        x = self.stack.pop()
        if x == self.MinStack[-1]:
            self.MinStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.MinStack[-1]
