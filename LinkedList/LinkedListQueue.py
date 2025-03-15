class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, item):
        new_node = Node(item)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        item = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from an empty queue")
        return self.front.data

    def is_empty(self):
        return self.front is None


if __name__ == "__main__":
    q = LinkedListQueue()
    q.enqueue(100)
    q.enqueue(200)
    print("Front element:", q.peek())            # 출력: 100
    print("Dequeue element:", q.dequeue())         # 출력: 100
    print("Front element after dequeue:", q.peek())# 출력: 200
