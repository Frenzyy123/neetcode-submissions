import string
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        s1_freq = {}
        s2_freq = {}
        for char in string.ascii_lowercase:
            s1_freq[char] = 0
            s2_freq[char] = 0
        for char in s1:
            s1_freq[char] += 1
        for i in range(len(s1)):
            s2_freq[s2[i]] += 1
        s2_pointer = len(s1)
        for s2_pointer in range(s2_pointer,len(s2)):
            status = True
            for char in s1_freq:
                if s1_freq[char] != s2_freq[char]:
                    status = False
                    break
            if status :
                return True
            else:
                s2_freq[s2[s2_pointer - len(s1)]] -= 1
                s2_freq[s2[s2_pointer]] += 1

        for char in s1_freq:
            if s1_freq[char] != s2_freq[char]:
                return False
            
        return True