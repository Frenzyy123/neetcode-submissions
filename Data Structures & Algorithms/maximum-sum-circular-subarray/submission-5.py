class Solution:
    def maxSubarraySumCircular(self,nums: List[int]) -> int:
        if max(nums) < 0:
            return max(nums)
        globalMax,globalMin = nums[0],nums[0]
        curMax,curMin = 0,0
        total = 0
        for i in nums:
            total += i
            curMax = max(curMax + i,i)
            curMin = min(curMin + i,i)
            globalMax = max(globalMax,curMax)
            globalMin = min(globalMin,curMin)


        return max(globalMax,total - globalMin) 