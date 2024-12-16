from collections import deque
queue = deque()

def fn1(items):
    print('items',items)
    return items

fn1([1,2,3])

while queue:
    item = queue.popleft()
    print('item',item)


