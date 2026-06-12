"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[ListNode]') -> 'Optional[ListNode]':
        if not head:
            return 
        old_new_nodes = {}
        nodes_to_random = {}
        curr = head
        ran_curr = head
        while ran_curr:
            nodes_to_random[ran_curr] = ran_curr.random
            ran_curr = ran_curr.next
        while curr:
            old_new_nodes[curr] = Node(curr.val)
            curr = curr.next
        curr2 = head.next
        new_head = old_new_nodes[head]
        new_curr = new_head
        while curr2:
            new_curr.next = old_new_nodes[curr2]
            new_curr = new_curr.next
            curr2 = curr2.next
        curr3 = head
        while curr3:
            if nodes_to_random[curr3] is not None:
                old_new_nodes[curr3].random = old_new_nodes[nodes_to_random[curr3]]
            curr3 = curr3.next
        return new_head