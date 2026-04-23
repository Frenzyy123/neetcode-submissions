# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def backtrack(root,suma):
            if not root:
                return False
            suma += root.val            
            if not root.left and not root.right and suma == targetSum:
                return True
            if backtrack(root.left,suma) == True:
                return True
            if backtrack(root.right,suma) == True:
                return True
            return False
        return backtrack(root,0)