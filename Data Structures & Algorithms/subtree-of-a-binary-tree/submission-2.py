from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(root1,root2):
            if root1 is None and root2 is not None:
                return False
            elif root1 is not None and root2 is None:
                return False
            elif root1 is not None and root2 is not None and root1.val != root2.val:
                return False
            elif root1 is None and root2 is None:
                return True
            if isSame(root1.left,root2.left) == False:
                return False
            if isSame(root1.right,root2.right) == False:
                return False
            return True
        first_tree = deque()
        first_tree.append(root)
        while first_tree:
            for i in range(len(first_tree)):
                node = first_tree.popleft()
                if node.val == subRoot.val:
                    if isSame(node,subRoot) == True:
                        return True
                if node.left:
                    first_tree.append(node.left)
                if node.right:
                    first_tree.append(node.right)
        return False
            