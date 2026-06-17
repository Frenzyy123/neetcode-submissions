# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or not lists[0]:
            return None
        def mergeSortedLists(head1,head2):

            dummy = ListNode()
            save_dummy = dummy
            curr1 = head1
            curr2 = head2
            while curr1 and curr2:
                if curr1.val <= curr2.val:
                    dummy.next = curr1
                    curr1 = curr1.next
                else:
                    dummy.next = curr2
                    curr2 = curr2.next
                dummy = dummy.next
            if curr1 :
                dummy.next = curr1
            elif curr2:
                dummy.next = curr2       
            return save_dummy.next
            
        for i in range(len(lists) - 1):
            lists[i + 1] = mergeSortedLists(lists[i],lists[i + 1])
        return lists[-1]