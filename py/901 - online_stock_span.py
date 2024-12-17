'''
    Input = 
    [[], [100], [80], [110], [70], [60], [75], [100], [85]]]
                                          ^
    Stack = [
        [60, 1]
        [70, 1]
        [110, 3]
    ]


'''
class StockSpanner:

    def __init__(self):
        self.stack = []
        

    def next(self, price: int) -> int:
        spans = 1

        while self.stack and self.stack[-1][0] <= price:
            spans += self.stack.pop()[1]

        self.stack.append([price,spans])
        return spans

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
