# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        our_curr = dummy
        curr1 = list1
        curr2 = list2
        while curr1 or curr2:
            if not curr1:
                while curr2:
                    our_curr.next = curr2
                    our_curr = our_curr.next
                    curr2 = curr2.next
            elif not curr2:
                while curr1:
                    our_curr.next = curr1
                    our_curr = our_curr.next
                    curr1 = curr1.next
            else:
                if curr1.val <= curr2.val:
                    our_curr.next = curr1
                    curr1 = curr1.next
                else:
                    our_curr.next = curr2
                    curr2 = curr2.next
                our_curr = our_curr.next
        return dummy.next
