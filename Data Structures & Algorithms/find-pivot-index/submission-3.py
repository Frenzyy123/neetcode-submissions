class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        curr_index = 0
        left_sum = 0
        right_sum = sum(nums) - nums[0]
        while left_sum != right_sum and curr_index < len(nums):
            left_sum += nums[curr_index]
            curr_index += 1
            if curr_index == len(nums):
                return -1
            right_sum -= nums[curr_index]
        return curr_index
