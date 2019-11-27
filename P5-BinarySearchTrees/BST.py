
class BinarySearchTree:
    def __init__(self, val):
        self.parent = None
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return "[Node: {0}, Left: {1}, Right:{2}]".format(self.val, self.left, self.right)


class BstFunctions:
    def __init__(self):
        self.tree_size = 0

    def tree_insert(self, tree, z):
        y = None
        x = tree
        while x is not None:
            y = x
            if z > y.val:
                x = x.right
            else:
                x = x.left
        # z.p = y
        if y is None:
            tree.val = z
        if y.val > z:
            y.left = BinarySearchTree(z)
        else:
            y.right = BinarySearchTree(z)

    def contains(self, tree, k):
        if tree is None:
            return tree
        elif k == tree.val:
            return tree
        elif k < tree.val:
            return self.contains(tree.left, k)
        else:
            return self.contains(tree.right, k)

    def inorder(self, tree):
        if tree is not None:
            self.inorder(tree.left)
            print(tree.val)
            self.inorder(tree.right)

    def size(self, tree):
        if tree is not None:
            self.tree_size += 1
            self.size(tree.left)
            self.size(tree.right)

    def smallest(self, tree):
        x = tree
        while x is not None:
            smallest = x.val
            x = x.left
        return smallest

    def largest(self, tree):
        x = tree
        while x is not None:
            largest = x.val
            x = x.right
        return largest

    def successor(self, tree, key):
        x = tree
        x.parent = None




        if key.right is not None:
            return self.smallest(key.right)
        y = None
        while y is not None and x == y.right:
            x = y
            y = y.parent
        return y


bst = BinarySearchTree(5)
bst.left = BinarySearchTree(3)
bst.right = BinarySearchTree(7)
bst.left.left = BinarySearchTree(2)
bst.left.right = BinarySearchTree(4)
bst.right.left = BinarySearchTree(6)
bst.right.right = BinarySearchTree(8)
print(bst)

bst_functions = BstFunctions()
bst_functions.tree_insert(bst, 9)
bst_functions.tree_insert(bst, 1)
print(bst)

print("Search", bst_functions.contains(bst, 7))
print("Search", bst_functions.contains(bst, 13))

bst_functions.inorder(bst)

bst_functions.size(bst)
print('Tree Size:', bst_functions.tree_size)
print("Smallest:", bst_functions.smallest(bst))
print("Largest:", bst_functions.largest(bst))
print("Successor:", bst_functions.successor(bst, bst.left.right))
