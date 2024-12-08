
# Solution #3
class Solution:
   def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        ln = head
        if not head or left == right:
            return head

        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next
        
        reversed_head = None
        curr = prev.next

        for _ in range (right - left + 1):
            curr.next, reversed_head, curr = reversed_head, curr, curr.next
        
        prev.next.next = curr
        prev.next = reversed_head

        return dummy.next

# Solution #2
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
   def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        ln = head
        if not head or left == right:
            return head

        dummy = ListNode(-1)
        prev = dummy

        for _ in range(left - 1):
            prev.next = ln
            prev = prev.next
            ln = ln.next
        
        reversed_head = None

        for _ in range (right - left + 1):
            ln.next, reversed_head, ln = reversed_head, ln, ln.next

        prev.next = reversed_head

        while prev.next:
            prev = prev.next
        
        prev.next = ln
        
        return dummy.next
        
# Solution #1
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
   def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        l = r = 1
        ln, rn = head, head

        if not head.next:
            return head

        dummy = ListNode(-1)
        prev = dummy

        while l < left:
            prev.next = ln
            prev = prev.next
            ln = ln.next
            l += 1
        while r < right:
            rn = rn.next
            r += 1
        
        c = r - l + 1
        
        reversed = None
        ln_ref = ln

        while ln_ref and c > 0:
            ln_ref.next, reversed, ln_ref = reversed, ln_ref, ln_ref.next
            c -= 1

        prev.next = reversed

        while prev.next:
            prev = prev.next
        
        prev.next = ln_ref
        
        return dummy.next

        
        
        


        


        

        


        
