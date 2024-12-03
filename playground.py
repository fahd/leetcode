'''
    1 - 2 - 3 - 4

save = head.next.next
-> 3 - 4
head.next.next = head
-> 2 -> 1
        h
prev = head
-> 2-> 1*

node = save

----------------------------

node => 3 - 4
if prev:
    prev.next = node.next
    -> 2 -> 1 -> 4

if node.next:
    save = node.next.next   
    node.next.next = node
else:
    save = node.next

node.next.next = node
    -> 2 -> 1 -> 4 -> 3

prev = node
    -> 2 -> 1 -> 4 -> 3 



'''

