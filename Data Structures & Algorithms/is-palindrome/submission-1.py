import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        lp = 0
        rp = len(s) - 1
        while lp < rp:
            while lp < rp and s[lp] not in string.ascii_lowercase and s[lp] not in string.ascii_uppercase and s[lp] not in string.digits:
                lp += 1
            while rp > lp and s[rp] not in string.ascii_lowercase and s[rp] not in string.ascii_uppercase and s[rp] not in string.digits:
                rp -= 1
            if s[lp].lower() != s[rp].lower():
                return False
            lp += 1
            rp -= 1
        return True
