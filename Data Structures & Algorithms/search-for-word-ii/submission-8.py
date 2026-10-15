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




class Solution:
  def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
      Trie = PrefixTree()
      output = []
      for word in words:
          Trie.insert(word)
      def dfs(row,col,visited,current_branch,current_word):
          if row < 0 or col < 0 or row == len(board) or col == len(board[0]) or (row,col) in visited:
              return
          if board[row][col] not in current_branch.children:
            return
          visited.add((row,col))
          current_word += board[row][col]
          current_branch = current_branch.children[board[row][col]]
          if current_branch.endOfWord == True:
              output.append(current_word)
              current_branch.endOfWord = False
          dfs(row + 1,col,visited,current_branch,current_word)
          dfs(row, col + 1,visited,current_branch,current_word)
          dfs(row,col - 1,visited,current_branch,current_word)
          dfs(row - 1,col,visited,current_branch,current_word)
          visited.remove((row,col))

      for i in range(len(board)):
          for j in range(len(board[0])):
              if board[i][j] in Trie.drvo.children:
                  dfs(i,j,set(),Trie.drvo,"")

      return output

