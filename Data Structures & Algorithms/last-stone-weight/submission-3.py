class Heap():
    def __init__(self):
        self.heap = [float("-inf")]

    def push(self,val):
        self.heap.append(val)
        index = len(self.heap) - 1
        while index // 2 > 0:
            parent = index // 2
            if self.heap[index] < self.heap[parent]:
                temp = self.heap[parent]
                self.heap[parent] = self.heap[index]
                self.heap[index] = temp
                index = index // 2
            else:
                break

    def pop(self):
        if len(self.heap) == 1:
            return None
        if len(self.heap) == 2:
            return self.heap.pop()

        minimum = self.heap[1]
        self.heap[1] = self.heap.pop()
        
        index = 1
        while True:
            if index * 2 + 1 < len(self.heap):
                if self.heap[index * 2 + 1] < self.heap[index * 2] and self.heap[index] > self.heap[index * 2 + 1]:
                    temp = self.heap[index]
                    self.heap[index] = self.heap[index * 2  + 1]
                    self.heap[index * 2 + 1] = temp
                    index = index * 2 + 1
                elif self.heap[index] > self.heap[index * 2]:
                    temp = self.heap[index]
                    self.heap[index] = self.heap[index * 2]
                    self.heap[index * 2] = temp
                    index = index * 2 
            elif index * 2 < len(self.heap) and self.heap[index] > self.heap[index * 2]:
                    temp = self.heap[index]
                    self.heap[index] = self.heap[index * 2]
                    self.heap[index * 2] = temp
                    index = index * 2 
            else:
                break
        return minimum

    def heapify(self, arr):
    # 0-th position is moved to the end
        arr.append(arr[0])
        self.heap = arr
        cur = (len(self.heap) - 1) // 2
        while cur > 0:
            # Percolate down
            i = cur
            while 2 * i < len(self.heap):
                if (2 * i + 1 < len(self.heap) and 
                self.heap[2 * i + 1] < self.heap[2 * i] and 
                self.heap[i] > self.heap[2 * i + 1]):
                    # Swap right child
                    tmp = self.heap[i]
                    self.heap[i] = self.heap[2 * i + 1]
                    self.heap[2 * i + 1] = tmp
                    i = 2 * i + 1
                elif self.heap[i] > self.heap[2 * i]:
                    # Swap left child
                    tmp = self.heap[i]
                    self.heap[i] = self.heap[2 * i]
                    self.heap[2 * i] = tmp
                    i = 2 * i
                else:
                    break
            cur -= 1
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)

        stones.append(0)
        return abs(stones[0])