class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lp = 0
        rp = len(nums) - 1
        while lp <= rp:
            mid = (lp + rp) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > nums[rp]:
                if target >= nums[lp] and target < nums[mid]:
                    rp = mid - 1
                else:
                    lp = mid + 1
            else:
                if target > nums[mid] and target <= nums[rp]:
                    lp = mid + 1
                else:
                    rp = mid - 1
        return -1