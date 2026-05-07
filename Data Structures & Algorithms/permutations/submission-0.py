class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perm = []
        output = []
        def backtrack():
            if len(perm) == len(nums):
                output.append(perm.copy())
                return
            for i in nums:
                if i not in perm:
                    perm.append(i)
                    backtrack()
                    perm.pop()

        backtrack()
        return output