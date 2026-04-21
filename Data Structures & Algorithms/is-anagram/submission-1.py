class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        letters_s = {}
        for char in s:
            if char not in letters_s:
                letters_s[char] = 1
            else:
                letters_s[char] += 1
        for char in t:
            if char not in letters_s:
                return False
            elif letters_s[char] == 0:
                return False
            else:
                letters_s[char] -= 1
        for i in letters_s:
            if letters_s[i] != 0:
                return False
        return True