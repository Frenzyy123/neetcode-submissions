class TrieNode():
    def __init__(self):
        self.letters = {}
        self.endOfWord = False
class PrefixTree:
    def __init__(self):
        self.Trie = TrieNode()

    def insert(self, word: str) -> None:
        curr_trie = self.Trie
        for char in word:
            if char not in curr_trie.letters:
                curr_trie.letters[char] = TrieNode()
            curr_trie = curr_trie.letters[char]
                
        curr_trie.endOfWord = True

    def search(self, word: str) -> bool:
        curr_trie = self.Trie
        for char in word:
            if char not in curr_trie.letters:
                return False
            else:
                curr_trie = curr_trie.letters[char]
        if curr_trie.endOfWord == True:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        curr_trie = self.Trie
        for char in prefix:
            if char not in curr_trie.letters:
                return False
            else:
                curr_trie = curr_trie.letters[char]
        return True        
