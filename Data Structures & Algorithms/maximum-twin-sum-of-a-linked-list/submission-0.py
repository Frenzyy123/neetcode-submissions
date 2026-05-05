# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head:
            return
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        #ovo reversuje drugu polovinu sad srednja noda (gornja sredina) pokazuje na None
        prev, cur = None, slow
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        start = head
        end = prev
        maksSuma = float("-inf")
        while  end:
            maksSuma = max(maksSuma,start.val + end.val)
            start = start.next
            end = end.next
        return maksSuma
        