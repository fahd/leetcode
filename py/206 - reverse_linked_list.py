class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        prev = None

        while node:
            save = node.next
            node.next = prev
            prev = node
            node = save
        
        return prev
