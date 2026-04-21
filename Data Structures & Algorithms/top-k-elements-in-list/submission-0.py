class Solution:
    def topKFrequent(self, nums, k: int) :
        frequencies = {}
        removed = set()
        output = []
        for _ in range(k):
            maks = float("-inf")
            max_el = None
            for i in nums:
                if i in removed:
                    continue
                if i not in frequencies :
                    frequencies[i] = 1
                else:
                    frequencies[i] += 1
                if frequencies[i] > maks:
                    maks = frequencies[i]
                    max_el = i
            output.append(max_el)
            removed.add(max_el)
            frequencies = {}

        return output