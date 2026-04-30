class Solution:
    def minSubArrayLen(self,target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        minimum = float("inf")
        suma = 0
        while  right < len(nums):
            suma += nums[right]
            while left <= right and suma >= target:
                curr_len = right - left + 1
                minimum = min(minimum,curr_len)
                suma -= nums[left]
                left += 1
            right += 1
        if minimum != float("inf") :
            return minimum
        return 0