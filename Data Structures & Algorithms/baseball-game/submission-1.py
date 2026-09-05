
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in operations:
            if i == '+':
                x = stack[-1]
                y = stack[-2]
                stack.append(x + y)
            elif i == 'D':
                stack.append(2 * stack[-1])
            elif i == 'C':
                stack.pop()
            else:
                stack.append(int(i))
        return sum(stack)
