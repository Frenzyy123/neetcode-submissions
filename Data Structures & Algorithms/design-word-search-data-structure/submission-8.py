class TrieNode():
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.recnik = TrieNode() 

    def addWord(self, word: str) -> None:
        current = self.recnik
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.endOfWord = True        

    def search(self, word: str) -> bool:
        def dfs(index,current):
            for i in range(index,len(word)):
                if word[i] in current.children:
                    current = current.children[word[i]]
                elif word[i] == '.':
                    if not current.children:
                      return False
                    for child in current.children:
                        if dfs(i + 1,current.children[child]) == True:
                            return True
                    return False
                else:
                    return False
            return current.endOfWord
        return dfs(0,self.recnik)


