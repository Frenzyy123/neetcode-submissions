"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        duplicates = {}
        duplicates[node] = Node(node.val)
        def dfs(node):
            for neighbor in node.neighbors:
                if neighbor in duplicates:
                    duplicates[node].neighbors.append(duplicates[neighbor])
                else:
                    duplicates[neighbor] = Node(neighbor.val)
                    duplicates[node].neighbors.append(duplicates[neighbor])
                    dfs(neighbor)
        dfs(node)

        return duplicates[node]