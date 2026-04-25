# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        preorder = deque(preorder)
        def build(preorder,inorder):
            if not preorder or not inorder:
                return
            root = TreeNode(preorder[0])
            root_index = None
            for i in range(len(inorder)):
                if inorder[i] == preorder[0]:
                    root_index = i
                    preorder.popleft()
                    break
            root.left = build(preorder,inorder[0:root_index])
            root.right = build(preorder,inorder[root_index + 1:])
            return root
        return build(preorder,inorder)