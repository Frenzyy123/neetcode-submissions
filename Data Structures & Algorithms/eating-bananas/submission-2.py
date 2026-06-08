class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        rightValue = max(piles)
        leftValue = 1
        currMin = rightValue
        while leftValue <= rightValue:
            mid = (leftValue + rightValue) // 2
            hours = h
            for i in piles:
                hours -= i // mid
                if i % mid != 0:
                    hours -= 1
            if hours >= 0:
                currMin = min(currMin,mid)
                rightValue = mid - 1
            else:
                leftValue = mid + 1
        return currMin