class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        curr_sum = nums[0]
        all_max = nums[0]
        for i in range(1,len(nums)):
            if nums[i] > curr_sum + nums[i]:
                curr_sum = nums[i]
            else:
                curr_sum += nums[i]
            all_max = max(all_max,curr_sum)
        return all_max
