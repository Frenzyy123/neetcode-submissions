from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        que = deque([root])
        good_nodes = 1
        while que:
            for i in range(len(que)):
                node = que.popleft()
                if node.left:
                    que.append(node.left)
                    if node.left.val >= node.val:
                        good_nodes += 1
                    else:
                        node.left.val = node.val
                if node.right:
                    que.append(node.right)
                    if node.right.val >= node.val:
                        good_nodes += 1
                    else:
                        node.right.val = node.val
        return good_nodes