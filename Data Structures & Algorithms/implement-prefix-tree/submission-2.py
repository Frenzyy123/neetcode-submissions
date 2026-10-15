class TrieNode():
    def __init__(self):
        self.children = {}
        self.endOfWord = False
class PrefixTree:
    def __init__(self):
        self.drvo = TrieNode()

    def insert(self, word: str) -> None:
        current = self.drvo
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.endOfWord = True


    def search(self, word: str) -> bool:
        current = self.drvo
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.endOfWord

    def startsWith(self, prefix: str) -> bool:
        current = self.drvo
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True
        