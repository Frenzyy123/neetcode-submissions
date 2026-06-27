class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        comb = []
        output = []
        def backtrack(opened,closed):
            if opened + closed == n * 2:
                output.append("".join(comb.copy()))
                return
            
            if opened < n :
                comb.append('(')
                backtrack(opened + 1,closed)
                comb.pop()
            if closed < n and closed < opened:
                comb.append(')')
                backtrack(opened,closed + 1)
                comb.pop()

        backtrack(0,0)
        return output