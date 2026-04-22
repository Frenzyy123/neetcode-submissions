class Solution:
    def longestConsecutive(self, nums) -> int:
        if not nums:
            return 0 
        number_of_cons = {}
        for i in nums:
            number_of_cons[i] = 1
        visited = set()
        maks = 1
        for i in number_of_cons:
            if i in visited:
                continue
            visited.add(i)
            temp = i
            temp += 1
            while temp in number_of_cons:
                if temp in visited:
                    number_of_cons[i] += number_of_cons[temp]
                    break
                number_of_cons[i] += 1
                visited.add(temp)
                temp += 1
            maks = max(maks,number_of_cons[i])
        return maks
