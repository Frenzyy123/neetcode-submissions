class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        bucket = [0,0,0]
        for i in nums:
            bucket[i] += 1        
        nums_index = 0
        bucket_index = 0
        while nums_index < len(nums) and bucket_index < len(bucket):
            for i in range(bucket[bucket_index]):
                nums[nums_index] = bucket_index
                nums_index += 1
            bucket_index += 1
