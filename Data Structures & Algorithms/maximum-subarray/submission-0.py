class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = max(nums)
        if maxSum < 0 :
            return maxSum
        currSum = 0
        for i in nums:
            currSum = max(currSum + i,0)
            maxSum = max(currSum,maxSum)
        return maxSum