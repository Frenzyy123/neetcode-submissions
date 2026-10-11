class Solution:
  def maxArea(self, heights: List[int]) -> int:
        lp = 0
        rp = len(heights) - 1
        water = 0
        while lp < rp:
                curr_water = (rp - lp) * min(heights[lp],heights[rp])
                water = max(curr_water,water)
                if heights[lp] <= heights[rp]:
                        lp += 1
                else:
                        rp -= 1
        return water

