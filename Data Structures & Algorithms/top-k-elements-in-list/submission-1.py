class Solution:
    def topKFrequent(self, nums, k: int) :
        if not nums:
            return 
        frequencies = {}
        distinct_array = []
        for i in nums:
            if i not in frequencies:
                frequencies[i] = 1
                distinct_array.append(i)
            else:
                frequencies[i] += 1
        
        new_frequenies = {}
        for i in range(len(nums),0,-1):
            new_frequenies[i] = []

        for i in distinct_array:
            new_frequenies[frequencies[i]].append(i)
        output = []
        finding_top_k = 0
        for i in range(len(nums),-1,-1):
            for num in new_frequenies[i]:
                output.append(num)
                finding_top_k += 1
                if finding_top_k == k:
                    return output

