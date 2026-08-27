class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = [None] * len(s)
        def dfs(index):
            if index == len(s):
                return True 
            if cache[index] is False:
                return False

            for word in wordDict:
                if len(word) + index <= len(s) and s[index:index + len(word)] == word:
                    if dfs(index + len(word)) == True:
                        return True
            
            cache[index] = False
            return False

        return dfs(0)