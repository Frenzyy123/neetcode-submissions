class Solution:
    def trap(self, height: List[int]) -> int:
        lp = 0
        total_water = 0
        while lp < len(height):
            while lp < len(height) - 1 and height[lp] < height[lp + 1]:
                lp += 1
            if lp == len(height) - 1:
                return total_water
            rp = lp + 1
            potential_water = 0
            while rp < len(height) and height[rp] < height[lp]:
                potential_water += height[lp] - height[rp]
                rp += 1
            if rp < len(height):
                total_water += potential_water
            else:
                new_rp = rp - 1
                new_iter = new_rp
                while new_iter > lp:
                    while new_iter > lp and height[new_iter] < height[new_iter - 1]:
                        new_iter -= 1
                    if new_iter == lp:
                        return total_water
                    save_point = new_iter
                    new_iter -= 1
                    while new_iter > lp and height[new_iter] < height[save_point]:
                        total_water += height[save_point] - height[new_iter]
                        new_iter -= 1
                    save_point = new_iter
                
            lp = rp
            
        return  total_water