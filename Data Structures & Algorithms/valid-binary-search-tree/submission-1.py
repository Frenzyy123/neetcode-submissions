# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root,currMin,currMax):
            if not root:
                return
            if root.val >= currMax:
                return False

            if root.val <= currMin:
                return False

            if dfs(root.left,currMin,root.val) == False:
                return False
            
            
            if dfs(root.right,root.val,currMax) == False:
                return False
            return True
        return dfs(root,float("-inf"),float("inf"))
