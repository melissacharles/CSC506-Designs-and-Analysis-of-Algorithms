import random

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self, array):
        self.root = self.build_tree(sorted(set(array)))

    def build_tree(self, array):
        if not array:
            return None
        mid = len(array) // 2
        root = Node(array[mid])
        root.left = self.build_tree(array[:mid])
        root.right = self.build_tree(array[mid+1:])
        return root

    def insert(self, value, node=None):
        if node is None:
            node = self.root
        if value < node.data:
            if node.left is None:
                node.left = Node(value)
            else:
                self.insert(value, node.left)
        elif value > node.data:
            if node.right is None:
                node.right = Node(value)
            else:
                self.insert(value, node.right)
        return node

    def delete(self, value, node=None):
        if node is None:
            node = self.root
        if node is None:
            return None
        if value < node.data:
            node.left = self.delete(value, node.left)
        elif value > node.data:
            node.right = self.delete(value, node.right)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self.min_value_node(node.right)
            node.data = temp.data
            node.right = self.delete(temp.data, node.right)
        return node

    def min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def is_balanced_helper(self, node):
        if node is None:
            return 0  # Height of the tree
        left_height = self.is_balanced_helper(node.left)
        if left_height == -1:
            return -1  # Not balanced
        right_height = self.is_balanced_helper(node.right)
        if right_height == -1:
            return -1  # Not balanced
        if abs(left_height - right_height) > 1:
            return -1  # Not balanced
        return max(left_height, right_height) + 1

    def balanced(self, node=None):
        if node is None:
            node = self.root
        return self.is_balanced_helper(node) != -1

    def rebalance(self):
        nodes = self.inorder_traversal(self.root, [])
        self.root = self.build_tree(nodes)

    def inorder_traversal(self, node, nodes):
        if node:
            self.inorder_traversal(node.left, nodes)
            nodes.append(node.data)
            self.inorder_traversal(node.right, nodes)
        return nodes

    def preorder_traversal(self, node, nodes):
        if node:
            nodes.append(node.data)
            self.preorder_traversal(node.left, nodes)
            self.preorder_traversal(node.right, nodes)
        return nodes

    def postorder_traversal(self, node, nodes):
        if node:
            self.postorder_traversal(node.left, nodes)
            self.postorder_traversal(node.right, nodes)
            nodes.append(node.data)
        return nodes

    def level_order_traversal(self, start):
        if start is None:
            return []
        queue = [start]
        result = []
        while queue:
            node = queue.pop(0)
            result.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result

# Driver script
random_numbers = [random.randint(1, 100) for _ in range(15)]
tree = Tree(random_numbers)

print("Balanced:", tree.balanced())
print("Level order traversal:", tree.level_order_traversal(tree.root))
print("Preorder traversal:", tree.preorder_traversal(tree.root, []))
print("Inorder traversal:", tree.inorder_traversal(tree.root, []))
print("Postorder traversal:", tree.postorder_traversal(tree.root, []))

# Try to unbalance the tree
for _ in range(5):
    tree.insert(500)

print("\nAfter insertions:")
print("Balanced:", tree.balanced())

# Rebalance the tree
tree.rebalance()

print("\nAfter rebalancing:")
print("Balanced:", tree.balanced())
print("Level order traversal:", tree.level_order_traversal(tree.root))
print("Preorder traversal:", tree.preorder_traversal(tree.root, []))
print("Inorder traversal:", tree.inorder_traversal(tree.root, []))


