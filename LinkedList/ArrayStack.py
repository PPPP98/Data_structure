class ArrayStack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        raise IndexError("Pop from an empty stack")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        raise IndexError("Peek from an empty stack")

    def is_empty(self):
        return len(self.stack) == 0

if __name__ == "__main__":
    s = ArrayStack()
    s.push(10)
    s.push(20)
    print("Top element:", s.peek())  # 출력: 20
    print("Pop element:", s.pop())   # 출력: 20