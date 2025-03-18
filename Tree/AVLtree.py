from BST import Node, BSTree


class AvlNode(Node):
    def __init__(self, data):
        super().__init__(data)
        self.height = 1


class AvlTree(BSTree):
    def __init__(self):
        self.root = None

    def get_height(self, node: AvlNode):
        """노드가 None이면 0, 아니면 해당 노드의 height를 반환"""
        if node is None:
            return 0
        return node.height

    def update_height(self, node: AvlNode):
        """노드의 높이를 좌우 자식 노드의 높이를 기반으로 갱신"""
        if node:
            node.height = 1 + max(
                self.get_height(node.left), self.get_height(node.right)
            )

    def get_balance(self, node: AvlNode):
        """해당 노드의 좌우 서브트리 높이 차이(균형 인자)를 반환"""
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def right_rotate(self, y: AvlNode):
        """오른쪽 회전: 불균형이 Left Left 혹은 Left Right 케이스일 때 사용"""
        x = y.left
        T2 = x.right

        # 회전 수행: x가 새로운 루트가 됨
        x.right = y
        y.left = T2

        # 높이 갱신
        self.update_height(y)
        self.update_height(x)
        return x

    def left_rotate(self, x: AvlNode):
        """왼쪽 회전: 불균형이 Right Right 혹은 Right Left 케이스일 때 사용"""
        y = x.right
        T2 = y.left

        # 회전 수행: y가 새로운 루트가 됨
        y.left = x
        x.right = T2

        # 높이 갱신
        self.update_height(x)
        self.update_height(y)
        return y

    def _insert(self, node: AvlNode, data):
        """재귀적으로 노드를 삽입하고, 삽입 후 균형을 맞춤"""
        if node is None:
            return AvlNode(data)
        if data < node.data:
            node.left = self._insert(node.left, data)
        else:
            node.right = self._insert(node.right, data)

        # 노드 높이 갱신
        self.update_height(node)

        # 균형 인자 계산
        balance = self.get_balance(node)

        # 균형이 깨진 경우, 4가지 케이스 처리

        # 1) Left Left Case
        if balance > 1 and data < node.left.data:
            return self.right_rotate(node)

        # 2) Right Right Case
        if balance < -1 and data > node.right.data:
            return self.left_rotate(node)

        # 3) Left Right Case
        if balance > 1 and data > node.left.data:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # 4) Right Left Case
        if balance < -1 and data < node.right.data:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def insert(self, data):
        """public 메서드: AVL 트리에 data 삽입"""
        self.root = self._insert(self.root, data)

    def _min_value_node(self, node: AvlNode):
        """해당 서브트리에서 가장 작은 값을 가진 노드를 반환"""
        current = node
        while current.left is not None:
            current = current.left
        return current

    def _delete(self, node: AvlNode, data):
        """재귀적으로 노드를 삭제하고, 삭제 후 균형을 맞춤"""
        if node is None:
            return node
        if data < node.data:
            node.left = self._delete(node.left, data)
        elif data > node.data:
            node.right = self._delete(node.right, data)
        else:
            # 삭제할 노드 발견
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp
            # 두 자식을 가진 경우: 오른쪽 서브트리의 최소값으로 대체
            temp = self._min_value_node(node.right)
            node.data = temp.data
            node.right = self._delete(node.right, temp.data)

        if node is None:
            return node

        # 높이 갱신 및 균형 인자 계산
        self.update_height(node)
        balance = self.get_balance(node)

        # 균형 케이스 처리
        # Left Left Case
        if balance > 1 and self.get_balance(node.left) >= 0:
            return self.right_rotate(node)
        # Left Right Case
        if balance > 1 and self.get_balance(node.left) < 0:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        # Right Right Case
        if balance < -1 and self.get_balance(node.right) <= 0:
            return self.left_rotate(node)
        # Right Left Case
        if balance < -1 and self.get_balance(node.right) > 0:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def delete(self, data):
        """public 메서드: AVL 트리에서 data 삭제"""
        self.root = self._delete(self.root, data)
    
    def inorder_traversal(self, node, result=None):
        if result is None:
            result = []
        if node:
            self.inorder_traversal(node.left, result)
            result.append(node.data)
            self.inorder_traversal(node.right, result)
        return result


if __name__ == "__main__":
    # AvlTree 인스턴스 생성
    avl = AvlTree()

    # 테스트용 데이터: 여러 값을 삽입하여 AVL 트리의 균형 상태를 확인
    values_to_insert = [30, 20, 40, 10, 25, 35, 50, 5]
    print("삽입할 값들:", values_to_insert)
    for value in values_to_insert:
        avl.insert(value)
        print(f"{value} 삽입 후 중위 순회:", avl.inorder_traversal(avl.root))

    # 특정 값 탐색 테스트
    search_value = 25
    found_node = avl.search(search_value)
    if found_node:
        print(f"탐색: 값 {search_value}가 트리에서 발견되었습니다.")
    else:
        print(f"탐색: 값 {search_value}를 찾을 수 없습니다.")

    # 삭제 연산 테스트
    delete_value = 20
    print(f"\n값 {delete_value} 삭제 전 중위 순회:", avl.inorder_traversal(avl.root))
    avl.delete(delete_value)
    print(f"값 {delete_value} 삭제 후 중위 순회:", avl.inorder_traversal(avl.root))

    # 추가 삭제 테스트: 루트 노드 삭제 등
    delete_value = 30
    print(f"\n값 {delete_value} 삭제 전 중위 순회:", avl.inorder_traversal(avl.root))
    avl.delete(delete_value)
    print(f"값 {delete_value} 삭제 후 중위 순회:", avl.inorder_traversal(avl.root))