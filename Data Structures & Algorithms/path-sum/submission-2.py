# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        def dfs(root,curr_sum,target):
            if not root:
                return False
            if root.left is None and root.right is None and curr_sum + root.val == target:
                return True
            if dfs(root.left,curr_sum + root.val,target) == True:
                return True
            if dfs(root.right,curr_sum + root.val,target) == True:
                return True
            return False
        return dfs(root,0,targetSum)