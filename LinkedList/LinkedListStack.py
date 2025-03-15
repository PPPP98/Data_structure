class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListStack:
    def __init__(self):
        self.top = None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        popped_node = self.top
        self.top = self.top.next
        return popped_node.data

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self.top.data

    def is_empty(self):
        return self.top is None

if __name__ == "__main__":
    s = LinkedListStack()
    s.push(100)
    s.push(200)
    print("Top element:", s.peek())  # 출력: 200
    print("Pop element:", s.pop())   # 출력: 200
