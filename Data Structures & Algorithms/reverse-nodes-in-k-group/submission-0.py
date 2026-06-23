# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def get_len(head):
            curr = head
            counter = 0
            while curr:
                counter += 1
                curr = curr.next
            return counter
        num_groups = get_len(head) // k
        curr = head
        prev = None
        save_first = curr
        for i in range(num_groups):
            new_save = curr
            for j in range(k):
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            if i == 0 :
                head = prev
            else:
                save_first.next = prev
                save_first = new_save
            prev = None
        new_save.next = curr
        return head
        