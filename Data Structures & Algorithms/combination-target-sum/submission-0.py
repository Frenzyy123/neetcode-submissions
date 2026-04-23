class Solution:
    def combinationSum(self, nums , target: int) :
        output = []
        comb = []
        def backtrack(index):
            if sum(comb) == target:
                output.append(comb.copy())
                return
            elif sum(comb) > target:
                return

            for i in range(index,len(nums)):
                comb.append(nums[i])
                backtrack(i)
                comb.pop()
        backtrack(0)
        return output