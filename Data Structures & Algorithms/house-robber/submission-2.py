class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        money = [0] * len(nums)
        money[0] = nums[0]
        money[1] = max(nums[0],nums[1])
        for i in range(2,len(money)):
            money[i] = max(money[i - 1],money[i - 2] + nums[i])
        return money[-1]