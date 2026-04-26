import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        updated_nums = [-x for x in nums]
        heapq.heapify(updated_nums)
        for i in range(k):
            el = heapq.heappop(updated_nums)
        return el * (-1)