class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        def backtrack(sub,index):
            output.append(sub.copy())
            for i in range(index,len(nums)):
                sub.append(nums[i])
                backtrack(sub,i + 1)
                sub.pop()
        backtrack([],0)
        return output