# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root) -> bool:
        if not root:
            return True
        def dfs(root):
            if not root:
                return 0
            if root.left is None and root.right is None:
                return 1
            left_height = dfs(root.left)
            if left_height is False:
                return False
            else:
                left_height += 1
            right_height =  dfs(root.right)
            if right_height is False:
                return False
            else:
                right_height += 1
            if abs(left_height - right_height) >= 2:
                return False
            else:
                return max(left_height,right_height)
        if dfs(root) == False:
            return False
        return True
