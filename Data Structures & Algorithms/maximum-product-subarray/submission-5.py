class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        res = nums[0]
        cur_min, cur_max = 1, 1
        
        for n in nums:
            # If we hit a 0, it resets our product chain
            if n == 0:
                cur_min, cur_max = 1, 1
                res = max(res, 0)
                continue
                
            # Temporarily store cur_max because it gets updated
            tmp = cur_max * n
            
            cur_max = max(n * cur_max, n * cur_min, n)
            cur_min = min(tmp, n * cur_min, n)
            
            res = max(res, cur_max)
            
        return res