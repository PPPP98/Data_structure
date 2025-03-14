class Node:
    def __init__(self, data):
        self.data = data
        self.left = None  # 왼쪽 자식
        self.right = None  # 오른쪽 자식


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        """완전 이진 트리 형태로 삽입"""
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            return

        # 레벨 순회로 빈 자리를 찾음
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            if current.left is None:
                current.left = new_node
                return
            else:
                queue.append(current.left)
            if current.right is None:
                current.right = new_node
                return
            else:
                queue.append(current.right)

    def delete(self, data):
        if self.root is None:
            print("트리가 비어 있습니다.")
            return

        # 삭제할 노드, 마지막 노드, 그리고 마지막 노드의 부모를 저장할 변수
        target_node = None
        last_node = None
        parent_of_last = None

        # 레벨 순회를 위해 큐 초기화
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            # 삭제할 노드를 찾으면 target_node에 저장
            if current.data == data:
                target_node = current

            # 왼쪽 자식 처리
            if current.left:
                parent_of_last = current
                last_node = current.left
                queue.append(current.left)
            # 오른쪽 자식 처리
            if current.right:
                parent_of_last = current
                last_node = current.right
                queue.append(current.right)

        if target_node is None:
            print(f"값 {data}가 트리에 존재하지 않습니다.")
            return

        # 삭제할 노드에 마지막 노드의 데이터를 덮어씀
        target_node.data = last_node.data

        # 마지막 노드를 삭제: parent_of_last의 자식 포인터에서 제거
        if parent_of_last:
            if parent_of_last.right == last_node:
                parent_of_last.right = None
            else:
                parent_of_last.left = None
        else:
            # 트리에 노드가 하나뿐인 경우(루트만 존재)
            self.root = None

    def pre_order(self, node, visit):
        """전위 순회: 현재 노드 → 왼쪽 → 오른쪽"""
        if node:
            visit.append(node.data)
            self.pre_order(node.left, visit)
            self.pre_order(node.right, visit)

    def in_order(self, node, visit):
        """중위 순회: 왼쪽 → 현재 노드 → 오른쪽"""
        if node:
            self.in_order(node.left, visit)
            visit.append(node.data)
            self.in_order(node.right, visit)

    def post_order(self, node, visit):
        """후위 순회: 왼쪽 → 오른쪽 → 현재 노드"""
        if node:
            self.post_order(node.left, visit)
            self.post_order(node.right, visit)
            visit.append(node.data)

    def level_order(self, visit):
        """레벨 순회: 같은 레벨의 노드를 좌에서 우로 방문"""
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            visit.append(current.data)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

if __name__ == "__main__":
    tree = BinaryTree()

    for i in range(1, 10):
        tree.insert(i)

    result = []
    tree.in_order(tree.root, result)
    print(result)
    result = []
    tree.pre_order(tree.root, result)
    print(result)
    result = []
    tree.post_order(tree.root, result)
    print(result)
    result = []
    tree.level_order(result)
    print(result)
