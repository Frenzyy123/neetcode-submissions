class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        left = 0
        right = 0
        visited = set()
        max_different = 1
        while right < len(s):
            if s[right] not in visited:
                while right < len(s) and s[right] not in visited:
                    visited.add(s[right])
                    right += 1
                    max_different  = max(max_different,right - left)
            else:
                visited.remove(s[left])
                left += 1
        
        return max_different