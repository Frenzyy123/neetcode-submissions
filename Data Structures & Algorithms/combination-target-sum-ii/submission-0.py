class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        comb = []
        output = []
        def backtrack(index,last_popped):
            if sum(comb) == target:
                output.append(comb.copy())
                return

            for i in range(index,len(candidates)):
                if sum(comb) + candidates[i] <= target:
                    if last_popped is not None and last_popped == candidates[i]:
                        continue
                    comb.append(candidates[i])
                    backtrack(i + 1,last_popped)
                    last_popped =  comb.pop()
                else:
                    return
        backtrack(0,None)
        return output