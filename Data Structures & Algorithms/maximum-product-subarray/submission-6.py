class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        sol = nums[0]
        curr_max = 1
        curr_min = 1
        for i in nums:
            if i == 0:
                curr_max = 1
                curr_min = 1
                sol = max(sol,0)
                continue

            prod = i * curr_max

            curr_max = max(prod,i * curr_min,i)
            curr_min = min(prod,i * curr_min,i)


            sol = max(sol,curr_max)
                            
        return sol