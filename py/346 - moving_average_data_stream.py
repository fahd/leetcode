from collections import deque
class MovingAverage:
    def __init__(self, size: int):
        self.window_size = size
        self.current_size = 0
        self.sum = 0
        self.queue = deque()
        

    def next(self, val: int) -> float:
        if self.current_size == self.window_size:
            self.sum -= self.queue[0]
            self.queue.popleft()
            self.current_size -= 1
        
        self.sum += val
        self.queue.append(val)
        self.current_size += 1

        return float(self.sum / self.current_size)
