#!/usr/bin/env python3
from binary_tree import BinaryTree

def inorder(node):
    if node is None:
        return []
    res = [node.item]
    left_item = inorder(node.left)
    right_item = inorder(node.right)
    return left_item + res + right_item


def preorder(node):
    if node is None:
        return []
    res = [node.item]
    left_item = preorder(node.left)
    right_item = preorder(node.right)
    return res + left_item + right_item

def postorder(node):
    if node is None:
        return []
    res = [node.item]
    left_item = postorder(node.left)
    right_item = postorder(node.right)
    return left_item + right_item + res


if __name__ == '__main__':
    tree = BinaryTree()
    for i in range(10):
        tree.add(i)
    tree.show_tree()
    print('inorder:', inorder(tree.root))
    print('preorder:', preorder(tree.root))
    print('postorder:', postorder(tree.root))

