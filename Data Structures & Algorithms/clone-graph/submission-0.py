"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self,node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        if not node.neighbors:
            return Node()
        nodes = {}
        nodes[node] = Node(node.val)
        def dfs(node,nodes):
            for neighbor in node.neighbors:
                if neighbor in nodes:
                    nodes[node].neighbors.append(nodes[neighbor])
                else:
                    nodes[neighbor] = Node(neighbor.val)
                    nodes[node].neighbors.append(nodes[neighbor])    
                    dfs(neighbor,nodes)
        dfs(node,nodes)
        return nodes[node]