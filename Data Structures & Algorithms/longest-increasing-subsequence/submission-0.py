class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = [1] * len(nums)
        def dfs(index):
            if index == len(nums) - 1:
                return 1
            if cache[index] != 1:
                return cache[index]
            for i in range(index + 1,len(nums)):
                if nums[index] < nums[i]:
                    cache[index] = max(cache[index],1 + dfs(i))
            return cache[index]
        for i in range(len(nums)):
            dfs(i)
        return max(cache)
        
