class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lp = 0
        rp = len(heights) - 1
        maks_area = min(heights[lp],heights[rp]) * (rp - lp)
        while lp < rp:
            curr_area = min(heights[lp],heights[rp]) * (rp - lp)
            maks_area = max(maks_area,curr_area)
            if heights[lp] >= heights[rp]:
                rp -=1
            else:
                lp += 1
        return maks_area