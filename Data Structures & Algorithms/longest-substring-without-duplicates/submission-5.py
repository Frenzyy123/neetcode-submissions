class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {}
        lp = 0
        rp = 0
        res = 0
        for rp in range(len(s)):
            if s[rp] not in chars:
                chars[s[rp]] = rp
            else:
                if lp <= chars[s[rp]]:
                    lp = chars[s[rp]] + 1
                chars[s[rp]] = rp
            res = max(res,rp - lp + 1)
        return res