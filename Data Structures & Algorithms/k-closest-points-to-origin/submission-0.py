import math
class Solution:
    def calculateDistance(self,pair):
        return math.sqrt((0 - pair[0]) ** 2 + (0 - pair[1]) ** 2)
    def quickSort(self,nums:list,start,end):
        if start >= end:
            return
        pivot = self.calculateDistance(nums[end])
        left = start
        for i in range(start,end):
            if self.calculateDistance(nums[i]) <= pivot:
                temp = nums[left] 
                nums[left] = nums[i]
                nums[i] =  temp
                left += 1

        temp = nums[end]
        nums[end] = nums[left]
        nums[left] = temp
        self.quickSort(nums,start,left - 1)
        self.quickSort(nums,left + 1,end)
        return nums
    def kClosest(self, points, k: int) :
        distances =  self.quickSort(points,0,len(points) - 1)
        return distances[0:k]
