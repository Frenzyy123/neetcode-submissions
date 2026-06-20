# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(root1,root2):
            if root1 is None and root2 is not None:
                return False
            elif root1 is not None and root2 is None:
                return False
            elif root1 is not None and root2 is not None and root1.val != root2.val:
                return False
            elif root1 is None and root2 is None:
                return True
            
            if dfs(root1.left,root2.left) == False:
                return False
            if dfs(root1.right,root2.right) == False:
                return False

            return True
        return dfs(p,q)
