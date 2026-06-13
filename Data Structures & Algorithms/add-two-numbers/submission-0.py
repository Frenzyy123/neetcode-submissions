# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        expo_l1 = 0
        expo_l2 = 0
        num1 = 0
        num2 = 0
        curr_l1 = l1
        curr_l2 = l2
        while curr_l1:
            num1 += (curr_l1.val) * (10 ** expo_l1)
            curr_l1 = curr_l1.next
            expo_l1 += 1
        while curr_l2:
            num2 += (curr_l2.val) * (10 ** expo_l2)
            curr_l2 = curr_l2.next
            expo_l2 += 1
        final_number = num1 + num2
        new_head = ListNode(final_number % 10)
        final_number = final_number // 10
        fin_curr = new_head
        while final_number > 0:
            fin_curr.next = ListNode(final_number % 10)
            fin_curr = fin_curr.next
            final_number = final_number // 10
        return new_head
