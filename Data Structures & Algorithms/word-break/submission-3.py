class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:          
        dp = [None] * (len(s) + 1)
        dp[len(s)] = True
        for i in range(len(s) - 1, -1 ,-1):
            for word in wordDict:
                if i + len(word) <= len(s) and s[i:i + len(word)] == word and dp[i + len(word)] == True:
                    dp[i] = True

        if dp[0] is None:
            return False
        return dp[0]
