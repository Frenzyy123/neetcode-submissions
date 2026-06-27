class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        output = []
        comb = []
        phone_number = {
            '2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],
            '5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],
            '8':['t','u','v'],'9':['w','x','y','z']
        }
        def backtrack(index):
            if len(comb) == len(digits):
                output.append("".join(comb.copy()))
                return
            for char in phone_number[digits[index]]:
                comb.append(char)
                backtrack(index + 1)
                comb.pop()
        
        backtrack(0)
        return output