class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]
        def dfs(r,c,visited):
            if r < 0 or c < 0 or r == len(image) or c == len(image[0]) or (r,c) in visited or image[r][c] != original_color:
                return
            if image[r][c] == original_color:
                image[r][c] = color
            visited.add((r,c))
            dfs(r,c - 1,visited)
            dfs(r,c + 1,visited)
            dfs(r - 1,c,visited)
            dfs(r + 1,c,visited)
        dfs(sr,sc,set())
        return image