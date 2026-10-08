class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lp = 0 
        rp = 0
        max_len = 0
        added_letters = set()
        while rp < len(s):
            while rp < len(s) and s[rp] not in added_letters:
                added_letters.add(s[rp])
                rp += 1
            curr_len = rp - lp
            max_len = max(max_len,curr_len)
            while rp < len(s) and lp < rp and s[lp] != s[rp]:
                added_letters.remove(s[lp])
                lp += 1
            lp += 1
            rp += 1
        return  max_len
