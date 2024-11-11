class Node:
    def __init__(self, val):
        self.val = val
        self.left: Node = None
        self.right: Node = None

class BinaryTree:
    def __init__(self):
        self.root: Node = None

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self.__insert_recursive(self.root, val)

    def __insert_recursive(self, node, val):
        if val < node.val:
            if node.left is None:
                node.left = Node(val)
            else:
                self.__insert_recursive(node.left, val)
        else:
            if node.right is None:
                node.right = Node(val)
            else:
                self.__insert_recursive(node.right, val)

    def search(self, val):
        return self.__search_recursive(self.root, val)

    def __search_recursive(self, node, val):
        if node is None or node.val == val:
            return node
        if val < node.val:
            return self.__search_recursive(node.left, val)
        return self.__search_recursive(node.right, val)


tree = BinaryTree()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(2)
tree.insert(4)
tree.insert(6)
tree.insert(8)
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(2)
tree.insert(4)
tree.insert(6)
tree.insert(8)

def print_leaf_nodes(root: Node):
    if not root:
        return
    if not (root.left or root.right):
        print(root.val)
        return
    print_leaf_nodes(root.left)
    print_leaf_nodes(root.right)

print_leaf_nodes(tree.root)
print('\n')


def count_nodes(root: Node):
    if not root:
        return 0

    return 1 + count_nodes(root.left) + count_nodes(root.right)

def count_edges(root: Node):
    return count_nodes(root) - 1

print(count_edges(tree.root))
