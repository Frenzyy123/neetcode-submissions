import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid_chars = []
        for char in s:
            if char in string.ascii_lowercase or char in string.ascii_uppercase:
                valid_chars.append(char.lower())
            elif char in string.digits:
                valid_chars.append(char)
        palind = "".join(valid_chars)
        lp = 0
        rp = len(palind) - 1
        while lp < rp:
            if palind[lp] != palind[rp]:
                return False
            lp += 1
            rp -= 1
        return True
