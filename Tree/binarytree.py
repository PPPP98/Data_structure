class Node:
    def __init__(self, data):
        self.data = data
        self.left = None   # 왼쪽 자식
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