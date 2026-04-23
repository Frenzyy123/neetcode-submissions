class Solution:
    def subsets(self, nums):
        output = []
        subset = []

        def backtrack(index):
            output.append(subset.copy())  # <-- move here

            for i in range(index, len(nums)):
                subset.append(nums[i])
                backtrack(i + 1)
                subset.pop()

        backtrack(0)
        return output