class Solution:
    def longestPalindrome(self, s: str) -> str:
        res_start = 0
        res_end = 1
        res_max_len = 1
        for i in range(len(s)):
            l = i
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r  - l + 1) > res_max_len:
                    res_max_len = r - l + 1
                    res_start = l
                    res_end = r + 1
                l -= 1
                r += 1
            l = i 
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r  - l + 1) > res_max_len:
                    res_max_len = r - l + 1
                    res_start = l
                    res_end = r + 1
                l -= 1
                r += 1
        return s[res_start:res_end]
