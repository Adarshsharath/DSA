class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0] * k
        self.front = 0
        self.rear = -1
        self.size = 0
        self.capacity = k

    def enQueue(self, value: int) -> bool:
        if self.size == self.capacity:
            return False

        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.size == 0:
            return False

        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.size == 0:
            return -1
        return self.queue[self.front]

    def Rear(self) -> int:
        if self.size == 0:
            return -1
        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity