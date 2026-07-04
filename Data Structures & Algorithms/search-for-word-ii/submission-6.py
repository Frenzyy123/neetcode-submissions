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


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        noviTraj = PrefixTree()
        output = []
        for word in words:
            noviTraj.insert(word)
        currTrie = noviTraj.Trie
        def dfs(traj,row,col,visited,curr_word):
            if row < 0 or row == len(board) or col < 0 or col == len(board[0]):
                return False

            if board[row][col] not in traj.letters:
                return False
            if (row,col) in visited:
                return False
            if board[row][col] in traj.letters:
                visited.add((row,col))
                curr_word += board[row][col]
                traj = traj.letters[board[row][col]]
                if traj.endOfWord == True:
                    traj.endOfWord = False
                    output.append(curr_word)
            dfs(traj,row + 1,col,visited,curr_word)
            dfs(traj,row,col + 1,visited,curr_word)
            dfs(traj,row - 1,col,visited,curr_word)
            dfs(traj,row,col - 1,visited,curr_word)
            visited.remove((row, col))
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in currTrie.letters:
                    dfs(currTrie,i,j,set(),"")
        return output


