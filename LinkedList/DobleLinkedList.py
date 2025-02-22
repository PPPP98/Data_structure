class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class MyDeque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    """
    파이썬에서는 객체의 불리언 값 평가를 할 때 먼저 bool 메서드를 찾고,
    없다면 len 메서드를 호출해서 0이면 False, 0이 아니면 True로 평가합니다.
    즉, 직접 __bool__을 정의하지 않더라도 __len__을 정의해두면,
    길이가 0일 때는 False처럼 동작하게 됩니다.
    """

    def __len__(self):
        return self.length

    def __str__(self):
        if self.head is None:
            return "Empty"
        else:
            res = "["
            node = self.head
            while node.next is not None:
                res += str(node.data) + ", "
                node = node.next
            return res + str(node.data) + "]"

    def __contains__(self, target):
        if self.head is None:
            return False
        # 순회 하면서 데이터 찾기
        node = self.head
        while node is not None:
            if node.data == target:
                return True
            node = node.next
        return False

    def appendleft(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = self.tail = new_node
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

    def append(self, data):
        if self.tail is None:
            new_node = Node(data)
            self.tail = self.head = new_node
        else:
            new_node = Node(data)
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def popleft(self):
        if self.head is None:
            return None
        else:
            node = self.head
            if self.length == 1:
                self.head = self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
            self.length -= 1
            return node.data

    def pop(self):
        if self.tail is None:
            return None
        else:
            node = self.tail
            if self.length == 1:
                self.tail = self.head = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None
            self.length -= 1
            return node.data


if __name__ == "__main__":
    que = MyDeque()
    for i in range(5):
        que.append(i)
    
    print(f"{4 in que}")
