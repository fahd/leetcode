# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
0. original
1 - 2 - 3 - 4 - 5
l
                r

1. find middle
1 - 2 - 3 - 4 - 5
        s
                f

2. reverse from middle
1 - 2 - 5 - 4 - 3
    
3. compare maxes
1 - 2 - 5 - 4 - 3
'''
class Solution:
    def reverse_linked_list(self, node: ListNode):
        prev = None
        
        while node:
            save = node.next
            node.next = prev
            prev = node
            node = save
        
        return prev

    def pairSum(self, head: Optional[ListNode]) -> int:
        s = f = head
        node = head
        n = 0
        c = 0
        # edge case -> only 2 values
        if not head.next.next:
            return head.val + head.next.val
        
        # find middle 
        while f and f.next:
            s = s.next
            f = f.next.next
            n += 1
        
        # reverse from middle at s
        s = self.reverse_linked_list(s)
        i = 0

        while i < n and s and node:
            c = max(c, node.val + s.val)
            node = node.next
            s = s.next
        return c
