from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque()
        result = {i : 0 for i in range(len(temperatures))}
        for i in range(len(temperatures)):
            if stack and temperatures[i] > temperatures[stack[-1]]:
                while stack and temperatures[i] > temperatures[stack[-1]]:
                    result[stack[-1]] = i - stack[-1]
                    stack.pop()
            stack.append(i)
        return [result[x] for x in result]