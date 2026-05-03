class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pivots = {}
        for i in range(len(nums)):
            pivots[i] = []
        left_total = 0
        for i in range(len(nums)):
            pivots[i].append(left_total)
            left_total += nums[i]
        right_total = 0
        for i in range(len(nums) -1 ,-1,-1):
            pivots[i].append(right_total)
            right_total += nums[i]
        for i in range(len(nums)):
            if pivots[i][0] == pivots[i][1]:
                return i
        return -1