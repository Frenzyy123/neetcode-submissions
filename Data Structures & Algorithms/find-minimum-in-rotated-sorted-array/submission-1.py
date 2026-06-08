class Solution:
    def findMin(self, nums: List[int]) -> int:
        lp  = 0
        rp = len(nums) - 1
        def right(pos,length):
            return (pos + 1) % length
        while lp <= rp :
            mid = (lp + rp) // 2
            if nums[mid] < nums[mid - 1] and nums[mid] < nums[right(mid,len(nums))]:
                return nums[mid]
            elif nums[mid] > nums[rp]:
                lp = mid + 1
            else:
                rp = mid - 1
        return nums[mid]

