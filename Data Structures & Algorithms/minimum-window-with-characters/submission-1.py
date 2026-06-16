class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t :
            return ""
        t_freq = {}
        win_freq = {}
        for char in t:
            if char not in t_freq:
                t_freq[char] = 1
                win_freq[char] = 0
            else:
                t_freq[char] += 1
        resLen = float("inf")
        left = 0
        have = 0 
        need = len(t_freq)
        res = ""
        for r in range(len(s)):
            char = s[r]
            if char in t_freq :
                win_freq[char] += 1
            
                if win_freq[char] == t_freq[char]:
                    have += 1
                    
            while have == need:
                if (r - left + 1) < resLen:
                    resLen = (r - left + 1)
                    res = s[left:r + 1]
                if s[left] in win_freq:
                    win_freq[s[left]] -= 1
                    if win_freq[s[left]] < t_freq[s[left]]:
                        have -= 1
                left += 1
        return res