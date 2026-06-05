class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == '(':
                stack.append('(')
            elif char == ')':
                if not stack:
                    return False
                x = stack.pop()
                if x != '(':
                    return False
            elif char == '{':
                stack.append("{")
            elif char == '}':
                if not stack:
                    return False
                x = stack.pop()
                if x != '{':
                    return False
            elif char == '[':
                stack.append("[")
            elif char == ']':
                if not stack:
                    return False
                x = stack.pop()
                if x != '[':
                    return False
        if not stack:
            return True
        return False