class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BSTree:
    def __init__(self):
        self.root = None

    def search(self, data):
        node = self.root
        while node:
            if node.data == data:
                return node
            elif node.data > data:
                node = node.left
            else:
                node = node.right
        return None

    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, node: Node, data):
        if node is None:
            return Node(data)
        if data < node.data:
            node.left = self._insert(node.left, data)
        else:
            node.right = self._insert(node.right, data)
        return node

    def delete(self, data):
        self.root = self._delete(self.root, data)

    def _delete(self, node: Node, data):
        if node is None:
            return node
        # 삭제할 노드를 찾기 위한 탐색
        if data < node.data:
            node.left = self._delete(node.left, data)
        elif data > node.data:
            node.right = self._delete(node.right, data)
        else:
            # 삭제할 노드를 찾은 경우
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            # 양쪽 자식이 모두 있을 경우
            else:
                # 찾은 노드의 오른쪽 트리의 가장 작은 값을 노드 자리로 올림
                temp = self._min_value_node(node.right)
                node.data = temp.data
                node.right = self._delete(node.right, temp.data)
        return node

    def _min_value_node(self, node: Node):
        while node.left:
            node = node.left
        return node

    def inorder_traversal(self, node: Node):
        if node:
            yield from self.inorder_traversal(node.left)
            yield node.data
            yield from self.inorder_traversal(node.right)

    def balancing(self):
        nodes = list(self.inorder_traversal(self.root))
        self.root = self._balancing(0, len(nodes) - 1, nodes)
    
    def _balancing(self, left, right, nodes):
        if left > right:
            return None
        mid = (left + right) // 2
        node = Node(nodes[mid])
        node.left = self._balancing(left, mid - 1, nodes)
        node.right = self._balancing(mid + 1, right, nodes)
        return node





if __name__ == "__main__":
    bst = BSTree()
    # 노드 삽입
    for key in [50, 30, 70, 20, 40, 60, 80]:
        bst.insert(key)

    # 중위 순회 출력 (정렬된 순서)
    print("중위 순회 결과:", list(bst.inorder_traversal(bst.root)))

    # 노드 삭제 후 중위 순회 출력
    bst.delete(20)
    print("노드 삭제 후 중위 순회:", list(bst.inorder_traversal(bst.root)))
