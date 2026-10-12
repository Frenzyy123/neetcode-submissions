class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
      products = [1] * len(nums)
      left_prod = 1
      right_prod = 1
      lp = 0
      rp = len(nums) - 1
      while lp < len(nums) and rp > -1:
        products[lp] *= left_prod
        products[rp] *= right_prod
        left_prod *= nums[lp]
        right_prod *= nums[rp]
        lp += 1
        rp -= 1
      return products
