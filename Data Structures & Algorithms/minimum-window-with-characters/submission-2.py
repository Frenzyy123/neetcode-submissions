class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        have = 0
        t_freq = {}
        window_freq = {}
        for char in t:
            if char not in t_freq:
                t_freq[char] = 1
                window_freq[char] = 0
            else:
                t_freq[char] += 1
        need = len(t_freq)
        res = ""
        resLen = float("inf")
        for right in range(len(s)):
            char = s[right]
            if char in window_freq:
                window_freq[char] += 1
                if window_freq[char] == t_freq[char]:
                    have += 1
            
            while have == need:
                currLen = right - left + 1
                if currLen < resLen:
                    resLen = currLen
                    res = s[left:right + 1]
                if s[left] in window_freq:
                    window_freq[s[left]] -= 1
                    if window_freq[s[left]] < t_freq[s[left]] :
                        have -= 1
                left += 1
        return res