class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        for i in range(n + 1):
            num = i
            counter = 0
            while num > 0:
                if num & 1 == 1:
                    counter += 1
                num = num >> 1
            output.append(counter)
        return output