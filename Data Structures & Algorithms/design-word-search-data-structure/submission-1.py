class TrieNode():
    def __init__(self):
        self.children = {}
        self.endOfWord = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        def dfs(curr,start):
            for i in range(start,len(word)):
                if word[i] in curr.children:
                    curr = curr.children[word[i]]
                elif word[i] == '.':
                    for char in curr.children:
                        if dfs(curr.children[char],i + 1) == True:
                            return True
                    return False
                else:
                    return False
            return curr.endOfWord
        return dfs(curr,0)