class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        for i in range(len(heights)):
            start = i
            while stack and stack[-1][1] >= heights[i]:
                start = stack[-1][0]
                height = stack[-1][1]
                curr_area = (i - start) * height
                maxArea = max(curr_area,maxArea)
                stack.pop()
            stack.append((start,heights[i]))
        while stack:
            index,height = stack.pop()
            curr_area = (len(heights) - index) * height
            maxArea = max(curr_area,maxArea)
        return maxArea