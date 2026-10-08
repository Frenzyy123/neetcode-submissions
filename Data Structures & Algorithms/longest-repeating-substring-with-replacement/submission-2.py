class Solution:
    def characterReplacement(self,s: str, k: int) -> int:
        freq = {}
        left = 0
        right = 0
        max_len = 0
        while right < len(s):
            if s[right] not in freq:
                freq[s[right]] = 1
            else:
                freq[s[right]] += 1
            max_freq = 1
            for i in freq:
                max_freq = max(max_freq,freq[i])
            length = right - left + 1
            if length - max_freq <= k:
                max_len =  max(max_len,length)
            else:
                freq[s[left]] -= 1
                left += 1
            right += 1
        return max_len