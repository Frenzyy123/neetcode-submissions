# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 1. Map values to indices for O(1) lookup
        inorder_map = {val: i for i, val in enumerate(inorder)}
        preorder_queue = deque(preorder)
        
        def build(left, right):
            # Base case: no more elements in this subtree
            if left > right:
                return None
            
            # 2. Get the root value from preorder
            root_val = preorder_queue.popleft()
            root = TreeNode(root_val)
            
            # 3. Find where this root splits the inorder list
            mid = inorder_map[root_val]
            
            # 4. Recursively build subtrees using pointers
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)
            
            return root
            
        return build(0, len(inorder) - 1)