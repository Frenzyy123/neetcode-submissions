class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_len = 1
        for i in range(len(s)):
            lp = i
            rp = i
            while lp > -1 and rp < len(s) and s[lp] == s[rp] :
                if rp - lp + 1 >= longest_len:
                    longest_len = rp - lp + 1
                    save_lp = lp
                    save_rp = rp
                lp -= 1
                rp += 1
            
            new_lp = i
            new_rp = i + 1
            while new_lp > -1 and new_rp < len(s) and s[new_lp] == s[new_rp]:
                if new_rp - new_lp + 1 >= longest_len:
                    longest_len = new_rp - new_lp + 1
                    save_lp = new_lp
                    save_rp = new_rp
                new_lp -= 1
                new_rp += 1
        return s[save_lp:save_rp + 1]