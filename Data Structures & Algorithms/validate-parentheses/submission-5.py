class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        suma = 0
        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
                suma += 1
            elif char == ')':
                suma -= 1
                if not stack or stack.pop() != '(':
                    return False
            elif char == ']':
                suma -= 1
                if not stack or stack.pop() != '[':
                    return False
            else:
                suma -= 1
                if not stack or stack.pop() != '{':
                    return False
        if suma != 0 :
            return False
        return True
                