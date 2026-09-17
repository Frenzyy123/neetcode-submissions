class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        sub = []
        def dfs(index):
            if index >= len(nums):
                output.append(sub.copy())
                return
            
            sub.append(nums[index])
            dfs(index + 1)

            sub.pop()
            dfs(index + 1)

        dfs(0)
        return output