# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
1 - 2
    n
    c
'''
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        node = head
        curr = head.next

        while curr:
            while node and curr and node.val == curr.val:
                node.next = curr.next
                curr = node.next

            node = node.next

            if curr:
                curr = curr.next
            

        return head
