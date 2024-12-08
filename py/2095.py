class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head.next
        iterated = False
        slow = fast = head
        slower = None

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if not iterated:
                iterated = True
                slower = head
            else:
                slower = slower.next
        
        slower.next = slower.next.next

        return head
