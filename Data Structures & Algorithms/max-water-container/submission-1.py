class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maksArea = float("-inf")
        lp = 0
        rp = len(heights) - 1
        while lp < rp:
            currArea = min(heights[lp],heights[rp]) * (rp - lp)
            maksArea = max(currArea,maksArea)
            if heights[lp] <= heights[rp]:
                lp += 1
            else:
                rp -= 1
        return maksArea
