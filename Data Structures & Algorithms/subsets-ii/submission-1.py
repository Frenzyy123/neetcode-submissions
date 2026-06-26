class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sub = []
        output = []
        def backtrack(index):
            output.append(sub.copy())
            for i in range(index,len(nums)):
                if i > index and nums[i] == nums[i-1]:
                    continue
                sub.append(nums[i])
                backtrack(i + 1)
                sub.pop()
        backtrack(0)
        return output