class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(word):
            if not word:
                return False
            lp = 0
            rp = len(word) - 1
            while lp < rp:
                if word[lp] != word[rp]:
                    return False
                lp += 1
                rp -= 1
            return True

        output = []
        sub =  []
        def backtrack(start,end):
            if start == end:
                output.append(sub.copy())
                return
            for i in range(start,end):
                if isPalindrome(s[start : i + 1]) == True:
                    sub.append(s[start : i + 1])
                    backtrack(i + 1,end)
                    sub.pop()
        backtrack(0,len(s))
        return output

