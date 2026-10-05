class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if max(nums) < 0:
            return max(nums)
        curr_max = nums[0]
        all_max = nums[0]
        curr_min = nums[0]
        all_min = nums[0]
        for i in range(1,len(nums)):
            if nums[i] < nums[i] + curr_min:
                curr_min = nums[i]
            else:
                curr_min += nums[i]
            if nums[i] > nums[i] + curr_max:
                curr_max = nums[i]
            else:
                curr_max += nums[i]

            all_max = max(all_max,curr_max)
            all_min = min(all_min,curr_min)

        return max(sum(nums) - all_min,all_max)