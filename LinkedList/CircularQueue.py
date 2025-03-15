class CircularQueue:
    def __init__(self, capacity=5):
        self.capacity = capacity              # 큐의 최대 크기
        self.queue = [None] * capacity        # 고정 크기 배열 생성
        self.front = 0                        # 삭제(Dequeue) 위치
        self.rear = 0                         # 삽입(Enqueue) 위치
        self.size = 0                         # 현재 큐에 저장된 원소 개수

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, item):
        if self.is_full():
            raise OverflowError("Circular Queue is full")
        self.queue[self.rear] = item
        # 원형 구조를 위해 rear 인덱스 갱신 (모듈러 연산)
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Circular Queue is empty")
        item = self.queue[self.front]
        self.queue[self.front] = None  # 선택 사항: 메모리 해제
        # 원형 구조를 위해 front 인덱스 갱신 (모듈러 연산)
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("Circular Queue is empty")
        return self.queue[self.front]


if __name__ == "__main__":
    cq = CircularQueue(capacity=5)
    cq.enqueue(10)
    cq.enqueue(20)
    cq.enqueue(30)
    print("Front element:", cq.peek())  # 출력: 10

    print("Dequeue element:", cq.dequeue())  # 출력: 10
    cq.enqueue(40)
    cq.enqueue(50)
    cq.enqueue(60)  # 큐가 꽉 차는 경우

    # 현재 큐의 상태를 출력 (원형 배열 구조)
    print("Queue state:", cq.queue)
