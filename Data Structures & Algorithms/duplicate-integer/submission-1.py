class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check_duplicates = set()
        for i in nums:
            if i not in check_duplicates:
                check_duplicates.add(i)
            else:
                return True
        return False