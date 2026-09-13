class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        high = max(piles)
        low = 1
        while low <= high:
            mid = (low + high) // 2
            hours = 0
            for i in piles:
                if i < mid:
                    hours += 1
                else:
                    hours += i // mid
                    if i % mid != 0:
                        hours += 1
            if hours > h:
                low = mid + 1
            else:
                save = mid
                high = mid - 1
        return save