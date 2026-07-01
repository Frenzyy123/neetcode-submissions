class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        def helprob(arr:list):
            if len(arr) < 3:
                return max(arr)
            dp = [0] * (len(arr))
            dp[0] = arr[0]
            dp[1] = max(dp[0],arr[1])
            for i in range(1,len(arr)):
                dp[i] = max(arr[i] + dp[i - 2],dp[i - 1])
            return dp[-1]
        value_1 = helprob(nums[0:len(nums) - 1])
        value_2 = helprob(nums[1:])
        return max(value_1,value_2)