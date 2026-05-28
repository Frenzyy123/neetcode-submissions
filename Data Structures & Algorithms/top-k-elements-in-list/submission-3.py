class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return
        frequencies = {}
        for i in nums:
            if i not in frequencies:
                frequencies[i] = 1
            else:
                frequencies[i] += 1
        ocurrances = {}
        for i in frequencies:
            if frequencies[i] not in ocurrances:
                ocurrances[frequencies[i]] = [i]
            else:
                ocurrances[frequencies[i]].append(i)
        output = []
        for i in range(len(nums),0,-1):
            if k == 0:
                return output
            if i in ocurrances:
                for j in ocurrances[i]:
                    output.append(j)
                    k -= 1
            
        return output