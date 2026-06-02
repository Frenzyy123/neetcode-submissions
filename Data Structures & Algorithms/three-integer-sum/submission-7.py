class Solution:
    def threeSum(self, nums):
        nums.sort()
        output  = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            start_index = i + 1
            end_index = len(nums) - 1
            while start_index < end_index:
                total = nums[i] + nums[start_index] + nums[end_index]
                if total == 0:
                    output.append([nums[i],nums[start_index],nums[end_index]])
                    start_index += 1
                    while start_index < end_index and nums[start_index] == nums[start_index - 1]:
                        start_index += 1
                elif total < 0:
                    start_index += 1
                else:
                    end_index -= 1

            
        return output
            
            
