class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def __contains__(self, data):
        node = self.root
        while node:
            if node.data == data:
                return True
            elif node.data > data:
                node = node.left
            else:
                node = node.right
        return False
    
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return
        
        node = self.root
        while node is not None:
            parent = node
            if node.data > data:
                node = node.left
            else:
                node = node.right

        if parent.data > data:
            parent.left = Node(data)
        else:
            parent.right = Node(data)
        
    def find_min(self, node):
        """오른쪽 서브트리에서 최소값(가장 왼쪽 노드)을 찾습니다."""
        current = node
        while current.left:
            current = current.left
        return current

    def delete_node(self, node, data):
        """
        이진 탐색 트리에서 key에 해당하는 노드를 삭제하고, 
        삭제 후의 트리의 루트 노드를 반환합니다.
        """
        if node is None:
            return node  # 삭제할 노드가 없는 경우

        # 삭제할 노드가 현재 노드보다 작으면 왼쪽 서브트리로 이동
        if data < node.data:
            node.left = self.delete_node(node.left, data)
        # 삭제할 노드가 현재 노드보다 크면 오른쪽 서브트리로 이동
        elif data > node.data:
            node.right = self.delete_node(node.right, data)
        else:
            # 삭제할 노드를 찾은 경우

            # 1. 자식이 하나도 없는 경우 또는 한쪽 자식만 존재하는 경우
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # 2. 자식이 두 개인 경우
            # 오른쪽 서브트리에서 중위 후계자(최소값 노드)를 찾습니다.
            temp = self.find_min(node.right)
            # 현재 노드의 값을 후계자의 값으로 대체
            node.data = temp.data
            # 오른쪽 서브트리에서 후계자 노드를 삭제
            node.right = self.delete_node(node.right, temp.data)

        return node