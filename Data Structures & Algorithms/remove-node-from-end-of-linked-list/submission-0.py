# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return
        dummy = ListNode(0)
        dummy.next = head
        size = 0
        curr = head
        while curr:
            curr = curr.next
            size += 1
        find_pos = size - n
        new_curr = dummy
        pos = 0
        while pos < find_pos:
            new_curr = new_curr.next
            pos += 1
        new_curr.next  = new_curr.next.next
        return dummy.next