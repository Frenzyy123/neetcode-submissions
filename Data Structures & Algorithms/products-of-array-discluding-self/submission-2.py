class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [1] * len(nums)
        left_prod = 1
        for lp in range(len(nums)):
            products[lp] *= left_prod
            left_prod *= nums[lp]
        right_prod = 1
        for rp in range(len(nums) - 1, -1,-1):
            products[rp] *= right_prod
            right_prod *= nums[rp]
        
        return products