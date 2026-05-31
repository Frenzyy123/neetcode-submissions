class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        index_values = {x : 1 for x in nums}
        maks = 1
        for i in nums:
            temp = i - 1
            while temp in index_values:
                index_values[i] += index_values[temp]
                maks = max(maks,index_values[i])
                del index_values[temp]
                temp -= 1

        return maks