"""Функції пошуку максимального мінімального елементу, та видалення елементу
 бінарного дерева"""
from sys import maxsize


class Tree:

    def __init__(self, id_node):
        self.key = id_node
        self.left = None
        self.right = None


INT_MAX = maxsize
INT_MIN = -maxsize
MESS = "Inorder traversal of the given tree"


def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)


def insert(node, key):
    """A function to inserting a new node with given id_node"""
    # If the tree is empty,
    # return a new node
    if node is None:
        return Tree(key)

    # Otherwise recur down the tree
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    # return the (unchanged) node pointer
    return node


def print_min_max(element: Tree):
    """Function to print a maximum and minimum element in a tree"""
    if element is None:
        print("Tree is empty")
        return
    current = element
    pre = Tree(0)
    # Max variable for storing maximum value
    max_value = INT_MIN
    # Min variable for storing minimum value
    min_value = INT_MAX
    while current is not None:
        # If left child does nor exists
        if current.left is None:
            max_value = max(max_value, current.key)
            min_value = min(min_value, current.key)
            current = current.right
        else:
            # Find the inorder predecessor of current
            pre = current.left
            while pre.right is not None and pre.right != current:
                pre = pre.right
            # Make current as the right child of its inorder predecessor
            if pre.right is None:
                pre.right = current
                current = current.left
            # Revert the changes made in the 'if' part to
            # restore the original tree i.e., fix the
            # right child of predecessor
            else:
                pre.right = None
                max_value = max(max_value, current.key)
                min_value = min(min_value, current.key)
                current = current.right
            # End of if condition pre->right == NULL
        # End of if condition current->left == NULL
    print("\nMax value is :", max_value)
    print("Min value is :", min_value)


def delete_node(node, key):
    """Function of deletion the id_node and returns the new root_from_list"""
    if node is None:
        return node
    if key < node.key:
        node.left = delete_node(node.left, key)
        return node

    elif key > node.key:
        node.right = delete_node(node.right, key)
        return node

    if node.left is None and node.right is None:
        return None

    if node.left is None:
        temp = node.right
        node = None
        return temp

    elif node.right is None:
        temp = node.left
        node = None
        return temp

    succ_parent = node
    succ = node.right
    while succ.left is not None:
        succ_parent = succ
        succ = succ.left

    if succ_parent != node:
        succ_parent.left = succ.right
    else:
        succ_parent.right = succ.right

    node.key = succ.key
    return node


root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)

print(MESS)
inorder(root)
print_min_max(root)

print("\nDelete 20")
root = delete_node(root, 20)
print(MESS)
inorder(root)
print_min_max(root)

print("\nDelete 30")
root = delete_node(root, 30)
print(MESS)
inorder(root)
print_min_max(root)

print("\nDelete 50")
root = delete_node(root, 50)
print(MESS)
inorder(root)
print_min_max(root)
