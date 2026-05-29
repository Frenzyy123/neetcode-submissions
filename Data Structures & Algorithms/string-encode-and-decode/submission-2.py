class Solution:

    def encode(self, strs: List[str]) -> str:
        code = ""
        for s in strs:
            code += str(len(s)) + "#" + s
        return code
    def decode(self, s: str) -> List[str]:
        output = []
        start_index = 0
        iterating_index = 0
        while start_index < len(s) and iterating_index < len(s):
            while iterating_index < len(s) and s[iterating_index] != '#':
                iterating_index += 1
            if iterating_index == len(s):
                output.append(s[start_index:iterating_index])
                return output
            word_len = int(s[start_index:iterating_index])
            start_index = iterating_index + 1
            output.append(s[start_index:start_index + word_len])
            start_index += word_len
            iterating_index = start_index 
        return output