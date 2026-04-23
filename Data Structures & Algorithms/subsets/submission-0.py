class Solution:
    def subsets(self, nums):
        output = []
        output.append([])
        subset = []
        def backtrack(index):
            for i in range(index,len(nums)):
                subset.append(nums[i])
                backtrack(i + 1)
                output.append(subset.copy())
                subset.pop()

        backtrack(0)
        return output