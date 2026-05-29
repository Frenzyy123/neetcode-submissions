class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        pos = 0
        while pos < len(s):
            second_pos = pos
            while s[second_pos] != '#':
                second_pos += 1
            length = int(s[pos:second_pos])
            res.append(s[second_pos + 1:second_pos + 1 + length])
            pos = second_pos + 1 + length
        return res