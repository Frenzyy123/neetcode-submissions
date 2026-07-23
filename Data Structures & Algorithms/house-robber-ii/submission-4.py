class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        cut_last = nums[0:len(nums) - 1]
        cut_first = nums[1:]
        def bounty(arr:list):
            if len(arr) < 3:
                return max(arr)
            dp = [0] * len(arr)
            dp[0] = arr[0]
            dp[1] = max(arr[0],arr[1])
            for i in range(2,len(arr)):
                dp[i] = max(dp[i - 1],dp[i - 2] + arr[i])
            return dp[-1]
        return max(bounty(cut_last),bounty(cut_first))
