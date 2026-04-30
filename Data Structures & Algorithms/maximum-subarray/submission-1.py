class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currSum = nums[0]
        for i in nums[1:]:
            currSum = max(i,currSum + i)
            maxSum = max(currSum,maxSum)
        return maxSum