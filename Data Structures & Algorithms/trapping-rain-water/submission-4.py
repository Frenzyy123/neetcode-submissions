class Solution:
    def trap(self, height) -> int:
        lp = 0
        area = 0
        while lp < len(height) - 1:
            subtract_area = 0
            while lp < len(height) - 1 and height[lp] <= height[lp + 1]:
                lp += 1
            rp = lp + 1
            while rp < len(height) and height[rp] < height[lp]:
                subtract_area += height[rp]
                rp += 1
            if rp < len(height):
                area += height[lp] * (rp - lp - 1) - subtract_area
                lp = rp
            else:
                rp -= 1
                while rp > lp:
                    if height[rp] <= height[rp - 1]:
                        rp -= 1
                    else:
                        second_rp = rp - 1
                        subtract_area  = 0
                        while second_rp > lp and height[second_rp] < height[rp]:
                            subtract_area += height[second_rp]
                            second_rp -= 1
                        
                        area += height[rp] * (rp - second_rp - 1) - subtract_area
                        rp = second_rp
                return area
        return area