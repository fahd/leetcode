# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head
        for _ in range(n):
            fast = fast.next
        
        '''

        
        [1,2,3,4,5]
             s
                 f

        '''
        if not fast:
            return head.next
        
        while fast.next:
                slow = slow.next
                fast = fast.next
        
        slow.next = slow.next.next
        
        return head
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head

        if not head.next:
            return head.next

        for _ in range(n):
            fast = fast.next
        
        if fast == None:
            return slow.next

        while fast.next:
                slow = slow.next
                fast = fast.next
        if slow.next:
            slow.next = slow.next.next
        
        return head
        
