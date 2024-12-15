# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode(-1)
        node = dummy
        ref = head
        
        while ref:
            if ref.next:
                reversed = None
                curr = ref
                for _ in range(2):
                    curr.next, reversed, curr = reversed, curr, curr.next
                ref = curr
                node.next = reversed
                node = node.next.next
            else:
                node.next = ref
                ref = ref.next

        return dummy.next

'''
    [1,2,3,4]
     f
       s
    
    {} -> 2 -> 1* -> 3 -> 4
                     f
                          s
               p
                     n

    prev.next = second

    if not head or head.next:
        return head

    dummy = {
        val: -1,
        next: None
    }

    //
    {
        next: 2 -> 
    }

    //

    node = head

    // prev = dummy?


    while node and node.next:
        first = node
        second = node.next

        prev.next = second
        first.next = second.next
        second.next = first

        prev = node
        node = node.next



    return dummy.next






'''
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        node = head
        dummy = ListNode(0)
        prev = dummy

        while node and node.next:
            first = node
            second = node.next

            prev.next = second
            first.next = second.next
            second.next = first

            prev = node
            node = node.next
        
        return dummy.next

            
        
            
            

            
