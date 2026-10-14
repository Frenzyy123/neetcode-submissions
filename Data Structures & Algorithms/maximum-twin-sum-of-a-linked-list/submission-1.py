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
        tester = head
        counter = 0
        while tester:
            counter += 1
            tester = tester.next
        distance = counter - 1
        for i in range(counter // 2):
            fast = slow
            for j in range(distance):
                fast = fast.next
            curr_sum = slow.val + fast.val
            max_sum = max(curr_sum,max_sum)
            slow = slow.next
            distance -= 2
        return max_sum