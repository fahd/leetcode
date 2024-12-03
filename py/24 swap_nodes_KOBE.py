# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

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

            
        
            
            

            
