class TrieNode():
    def __init__(self):
        self.letters = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.Trie = TrieNode()        

    def addWord(self, word: str) -> None:
        curr_trie  = self.Trie
        for char in word:
            if char not in curr_trie.letters:
                curr_trie.letters[char] = TrieNode()
            curr_trie = curr_trie.letters[char]
        curr_trie.endOfWord = True

    def search(self, word: str) -> bool:
        curr_trie = self.Trie
        def dfs(curr_trie,index):
            if index == len(word):
                return curr_trie.endOfWord
            
            for char in curr_trie.letters:
                if word[index] != '.' and word[index] != char:
                    continue
                if dfs(curr_trie.letters[char],index + 1) == True:
                    return True
            return False
        for i in range(len(word)):
            if word[i] in curr_trie.letters:
                curr_trie = curr_trie.letters[word[i]]
            elif word[i] == '.':
                if dfs(curr_trie,i) == True:
                    return True
                else:
                    return False
            else:
                return False
        return curr_trie.endOfWord
