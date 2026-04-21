class Solution:
    from collections import defaultdict
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            sorted_word = "".join(sorted(word))
            groups[sorted_word].append(word)
        output = []
        for i in groups:
            output.append(groups[i])
        return output