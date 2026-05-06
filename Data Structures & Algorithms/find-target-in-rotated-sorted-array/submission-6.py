class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            middle = (start + end) // 2
            if target == nums[middle]:
                return middle
            if nums[middle] < nums[end]:
                if target > nums[middle] and target <= nums[end]:
                    start  = middle + 1
                else:
                    end = middle 
            else:
                if target >= nums[start] and target < nums[middle]:
                    end = middle 
                else:
                    start = middle + 1
            
        return - 1

        