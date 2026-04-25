# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMinNode(self,root):
        if not root:
            return
        while root and root.left:
            root = root.left
        return root
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return
        if root.val > key:
            root.left = self.deleteNode(root.left,key)
        elif root.val < key:
            root.right = self.deleteNode(root.right,key)
        else:
            if not root.left and not root.right:
                return None
            elif not root.left :
                return root.right
            elif not root.right:
                return root.left
            else:
                findMin = self.findMinNode(root.right)
                root.val = findMin.val
                root.right = self.deleteNode(root.right,root.val)
        return root