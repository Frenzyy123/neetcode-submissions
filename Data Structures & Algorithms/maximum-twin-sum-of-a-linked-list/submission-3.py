# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        curr_sum = 0
        max_sum = 0
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        curr = slow
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        new_curr = head
        while new_curr and prev:
            curr_sum = new_curr.val + prev.val
            new_curr = new_curr.next
            prev = prev.next
            max_sum = max(max_sum,curr_sum)
        return max_sum