class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def find(self, node: Node, parent: Node, val):
        if val == node.val:
            return True, node, parent
        if val < node.val and node.left:
            return self.find(node.left, node, val)
        if val > node.val and node.right:
            return self.find(node.right, node, val)
        return False, node, parent

    def add(self, node: Node):
        if self.root is None:
            self.root = node
            return node
        node_exists, n, p = self.find(self.root, None, node.val)
        if not node_exists:
            if node.val < n.val:
                n.left = node
            elif node.val > n.val:
                n.right = node
        return node
    
    def show_tree_wide(self, node: Node):
        if node is None:
            return
        current_level_nodes = [node]
        while current_level_nodes:
            next_level_nodes = []
            for node in current_level_nodes:
                print(node.val, end=" ")
                if node.left:
                    next_level_nodes.append(node.left)
                if node.right:
                    next_level_nodes.append(node.right)
            current_level_nodes = next_level_nodes
            print()

    def show_tree_deep(self, node: Node):
        if node is None:
            return
        
        self.show_tree_deep(node.left)
        print(node.val)
        self.show_tree_deep(node.right)


if __name__ == "__main__":
    tree = Tree()
    lst = [5, 3, 6, 9, 1, 4, 3, 8]
    for x in lst:
        tree.add(Node(x))
    tree.show_tree_deep(tree.root)
    tree.show_tree_wide(tree.root)