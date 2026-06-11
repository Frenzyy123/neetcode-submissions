# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def returnLastNode(head):
            curr = head
            while curr.next.next:
                curr = curr.next
            save = curr.next
            curr.next = None
            return save
        curr = head
        while curr.next and curr.next.next:
            temp = curr.next
            new = returnLastNode(curr)
            curr.next = new
            new.next = temp
            curr = temp
          #  glava.print_list()
        