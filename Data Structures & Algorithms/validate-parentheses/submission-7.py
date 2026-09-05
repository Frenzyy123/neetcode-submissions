class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {'[':']','(':')','{':'}'}
        stack = []
        for i in  s:
            if i in pairs:
                stack.append(i)
            else:
                if not stack:
                    return False
                x = stack.pop()
                if pairs[x] != i:
                    return False
        if not stack:
            return True
        return False
