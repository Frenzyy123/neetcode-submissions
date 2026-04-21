import string
from collections import defaultdict
class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        alpha_dict = {char: i + 1 for i, char in enumerate(string.ascii_lowercase)}
        places_for_letters = defaultdict(list)
        for word in strs:
            letters = [0] * 27
            for char in word:
                letters[alpha_dict[char]] += 1
            tupl_letters = tuple(letters)
            places_for_letters[tupl_letters].append(word)
        output = []
        for i in places_for_letters:
            output.append(places_for_letters[i])
        return output

