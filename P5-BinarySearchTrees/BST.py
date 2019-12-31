
class BinarySearchTree:
    def __init__(self, val):
        """
        Class for a Binary Search Tree Node object
        :param val:
        """
        self.parent = None
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return "[Node: {0}, Left: {1}, Right:{2}]".format(self.val, self.left, self.right)


class BstFunctions:
    def __init__(self):
        self.tree_size = 0
        self.sum_elements = 0

    def insert(self, tree, z):
        """
        Function to insert an element in the given Binary Search Tree
        :param tree: BST tree
        :param z: element that has to be inserted
        :return: BST with the element inserted
        """
        if tree is None:
            return BinarySearchTree(z)
        else:
            if z <= tree.val:
                temp = self.insert(tree.left, z)
                tree.left = temp
                temp.parent = tree
            else:
                temp = self.insert(tree.right, z)
                tree.right = temp
                temp.parent = tree
        return tree

    def contains(self, tree, k):
        """
        Function to search for an element in a Binary Search Tree
        :param tree:
        :param k:
        :return:
        """
        if tree is None:
            return tree
        elif k == tree.val:
            return tree
        elif k < tree.val:
            return self.contains(tree.left, k)
        else:
            return self.contains(tree.right, k)

    def inorder(self, tree):
        """
        Function to print the Binary Search Tree in increasing order
        :param tree:
        :return:
        """
        if tree is not None:
            self.inorder(tree.left)
            print(tree.val)
            self.inorder(tree.right)

    def size(self, tree):
        """
        Function to determine the size of Binary Search Tree
        :param tree:
        :return:
        """
        if tree is not None:
            self.tree_size += 1
            self.size(tree.left)
            self.size(tree.right)

    def smallest(self, tree):
        """
        Function to determine the smallest value in a Binary Search Tree
        :param tree:
        :return:
        """
        x = tree
        while x is not None:
            smallest = x.val
            x = x.left
        return smallest

    def largest(self, tree):
        """
        Function to determine the largest value in a Binary Search Tree
        :param tree:
        :return:
        """
        x = tree
        while x is not None:
            largest = x.val
            x = x.right
        return largest

    def successor(self, key):
        """
        Function to determine the successor of a key in a Binary Search Tree
        :param key:
        :return:
        """
        if key.right is not None:
            return self.smallest(key.right)
        p = key.parent
        while p is not None:
            if key != p.right:
                break
            key = p
            p = p.parent
        return p

    def predecessor(self, key):
        """
        Function to determine the predecessor of a key in a Binary Search Tree
        :param key:
        :return:
        """
        if key.left is not None:
            return self.largest(key.left)
        p = key.parent
        while p is not None:
            if key != p.left:
                break
            key = p
            p = p.parent
        return p

    def greater_sum_tree(self, tree):
        """
        Function to build a greater sum tree, initiates a DFS on the BST
        :param tree:
        :return:
        """
        self.dfs(tree)
        return tree

    def dfs(self, root):
        """
        Function to perform DFS starting from right most element and keep updating the sum of values visited and replace
        the node with the sum
        :param root:
        :return:
        """
        if root is None:
            return
        self.dfs(root.right)
        self.sum_elements += root.val
        root.val = self.sum_elements - root.val
        self.dfs(root.left)
        return


# Binary Tree Initialization
bst_functions = BstFunctions()
bst = None

bst = bst_functions.insert(bst, 5)
bst = bst_functions.insert(bst, 3)
bst = bst_functions.insert(bst, 7)
bst = bst_functions.insert(bst, 2)
bst = bst_functions.insert(bst, 4)
bst = bst_functions.insert(bst, 6)
bst = bst_functions.insert(bst, 8)
bst = bst_functions.insert(bst, 9)
bst = bst_functions.insert(bst, 1)
print(bst)
temp = bst.left.right.right

# Binary Tree Function
print("Searching for number 7:", bst_functions.contains(bst, 7))
print("Searching for number 13: ", bst_functions.contains(bst, 13))
print('Inorder print of Binary Search Tree')
bst_functions.inorder(bst)

bst_functions.size(bst)
print('Tree Size:', bst_functions.tree_size)
print("Smallest:", bst_functions.smallest(bst))
print("Largest:", bst_functions.largest(bst))
print('Element to find successor', bst_functions.contains(bst, 7).val)
print("Successor:", bst_functions.successor(bst_functions.contains(bst, 7)))

print('Element to find predecessor', bst_functions.contains(bst, 1).val)
print("Predecessor:", bst_functions.predecessor(bst_functions.contains(bst, 1)))

# print('Greater Sum Tree:', bst_functions.greater_sum_tree(bst))

print("Inorder before GST:", bst_functions.inorder(bst))
bst_functions.greater_sum_tree(bst)
print("Inorder after GST:", bst_functions.inorder(bst))

