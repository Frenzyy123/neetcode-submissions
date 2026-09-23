class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if sr < 0 or sr == len(image) or sc < 0 or sc == len(image[0]):
            return image
        orig = image[sr][sc]
        def dfs(row,col,visited):
            if row < 0 or row == len(image) or col < 0 or col == len(image[0]):
                return
            if (row,col) in visited:
                return
            visited.add((row,col))
            if image[row][col] == orig:
                image[row][col] = color
            else:
                return
            dfs(row + 1,col,visited)
            dfs(row,col + 1,visited)
            dfs(row - 1,col,visited)
            dfs(row,col - 1,visited)
        dfs(sr,sc,set())
        return image