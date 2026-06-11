# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        slow = head
        fast = head.next
        #nasli smo sredinu liste
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #hocemo da desnu polovinu reversujemo
        new = slow.next
        if not new:
            return 
        prev = new
        curr = new.next
        prev.next = None
        while curr :
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        slow.next = None
        lp = head
        rp = prev
        while rp :
            save_lp = lp.next
            save_rp = rp.next
            lp.next = rp
            rp.next = save_lp
            rp = save_rp
            lp = save_lp
        
        