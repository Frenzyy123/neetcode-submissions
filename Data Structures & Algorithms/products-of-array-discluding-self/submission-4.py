class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        left_prod = 1
        for i in range(len(nums) - 1):
            left_prod *= nums[i]
            output[i + 1] *= left_prod
        right_prod = 1
        for i in range(len(nums) -1,0,-1):
            right_prod *= nums[i]
            output[i - 1] *= right_prod
        return output