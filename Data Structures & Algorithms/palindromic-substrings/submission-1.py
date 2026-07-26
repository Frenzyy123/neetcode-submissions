class Solution:
    def countSubstrings(self, s: str) -> str:
        palind_counter = 0
        for i in range(len(s)):
            lp = i
            rp = i
            while lp > -1 and rp < len(s) and s[lp] == s[rp] :
                palind_counter += 1
                lp -= 1
                rp += 1
            
            new_lp = i
            new_rp = i + 1
            while new_lp > -1 and new_rp < len(s) and s[new_lp] == s[new_rp]:
                palind_counter += 1
                new_lp -= 1
                new_rp += 1
        return palind_counter