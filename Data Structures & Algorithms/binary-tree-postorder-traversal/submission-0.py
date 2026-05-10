# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        visit = [False]
        output = []
        while stack:
            curr = stack.pop()
            visited = visit.pop()
            if curr :
                if visited:
                    output.append(curr.val)
                else:
                    stack.append(curr)
                    visit.append(True)
                    if curr.right:
                        stack.append(curr.right)
                        visit.append(False)
                    if curr.left:
                        stack.append(curr.left)
                        visit.append(False)
        return output