# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_sofar):
            if not node:
                return 0
            good = 1 if node.val >= max_sofar else 0
            max_sofar = max(max_sofar, node.val)
            return good + dfs(node.left, max_sofar) + dfs(node.right, max_sofar)

        return dfs(root, root.val)