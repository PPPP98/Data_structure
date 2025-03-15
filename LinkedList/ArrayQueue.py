class ArrayQueue:
    def __init__(self, capacity=5):
        self.queue = [None] * capacity  # 고정 크기 배열
        self.capacity = capacity
        self.front = 0
        self.rear = 0
        self.size = 0

    def enqueue(self, item):
        if self.size == self.capacity:
            raise OverflowError("Queue is full")
        self.queue[self.rear] = item
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        item = self.queue[self.front]
        self.queue[self.front] = None  # Optional: Clear reference
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from an empty queue")
        return self.queue[self.front]

    def is_empty(self):
        return self.size == 0


if __name__ == "__main__":
    q = ArrayQueue(capacity=5)
    q.enqueue(10)
    q.enqueue(20)
    print("Front element:", q.peek())  # 출력: 10
    print("Dequeue element:", q.dequeue())  # 출력: 10
    print("Front element after dequeue:", q.peek())  # 출력: 20
