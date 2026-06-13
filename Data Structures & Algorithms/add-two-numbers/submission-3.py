# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #O(1) space
        curr_l1 = l1
        curr_l2 = l2
        while curr_l1 or curr_l2:
            over = 0
            while curr_l1 and curr_l2:
                suma = curr_l1.val + curr_l2.val + over
                if suma >= 10:
                    over = 1
                    suma -= 10
                else:
                    over = 0
                curr_l1.val = suma
                curr_l1 = curr_l1.next
                curr_l2 = curr_l2.next
            if curr_l1 is None and curr_l2 is None:
                if over == 1:
                    final_curr = l1
                    while final_curr.next:
                        final_curr = final_curr.next
                    final_curr.next = ListNode(1)
            elif curr_l1 is not None and curr_l2 is None:
                while curr_l1 :
                    suma = curr_l1.val + over
                    if suma == 10:
                        curr_l1.val = 0
                        over = 1
                    else:
                        curr_l1.val = suma
                        over = 0
                    curr_l1 = curr_l1.next
                if over == 1:
                    fp = l1
                    while fp.next:
                        fp = fp.next
                    fp.next = ListNode(1)
                
            elif curr_l1 is None and curr_l2 is not None:
                final_curr = l1
                while final_curr.next:
                    final_curr = final_curr.next
                while curr_l2:
                    suma = curr_l2.val + over
                    if suma >= 10:
                        final_curr.next = ListNode(suma - 10)
                        over = 1
                    else:
                        final_curr.next = ListNode(suma)
                        over = 0
                    final_curr = final_curr.next
                    curr_l2 = curr_l2.next
                if over == 1:
                    final_curr.next = ListNode(1)
                
        return l1