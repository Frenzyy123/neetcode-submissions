from math import sqrt
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        output = []
        for point in points:
            heap.append((sqrt(point[0]**2 + point[1]**2),point[0],point[1]))
        heapq.heapify(heap)
        for i in range(k):
            x = heapq.heappop(heap)
            output.append([x[1],x[2]])
        return output