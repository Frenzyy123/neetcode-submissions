# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0 
        max_depth = 0
        def dfs(root,curr_depth):
            nonlocal max_depth
            if not root:
                return
            max_depth = max(curr_depth,max_depth)
            dfs(root.left,curr_depth + 1)
            dfs(root.right,curr_depth + 1)
        dfs(root,1)
        return max_depth