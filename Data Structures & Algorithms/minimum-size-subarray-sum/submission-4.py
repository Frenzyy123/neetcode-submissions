class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        lp = 0
        rp = 0
        sol = float("inf")
        curr_sum = 0
        for rp in range(len(nums)):
            curr_sum += nums[rp]
            while curr_sum >= target and lp <= rp:
                sol = min(sol,rp - lp + 1)
                curr_sum -= nums[lp]
                lp += 1
        if sol == float("inf"):
            return 0
        return sol