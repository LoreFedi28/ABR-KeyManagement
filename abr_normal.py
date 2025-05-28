class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class ABRNormal:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_rec(self.root, key)

    def _insert_rec(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert_rec(node.left, key)
        elif key > node.key:
            node.right = self._insert_rec(node.right, key)
        # If the key is already present, do nothing (ignore duplicates)
        return node

    def search(self, key):
        return self._search_rec(self.root, key)

    def _search_rec(self, node, key):
        if node is None:
            return False
        if key == node.key:
            return True
        elif key < node.key:
            return self._search_rec(node.left, key)
        else:
            return self._search_rec(node.right, key)

    def in_order(self):
        return self._in_order_rec(self.root)

    def _in_order_rec(self, node):
        if node is None:
            return []
        return self._in_order_rec(node.left) + [node.key] + self._in_order_rec(node.right)