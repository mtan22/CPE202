from __future__ import annotations
from queue_array import Queue
from typing import Optional, Any, Tuple, List


class TreeNode:
    def __init__(self, key: Any, data: Any, left: Optional[TreeNode] = None, right: Optional[TreeNode] = None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right

    def __eq__(self, other: object) -> bool:
        if isinstance(other, TreeNode):
            return (self.key == other.key
                    and self.data == other.data
                    and self.left == other.left
                    and self.right == other.right)
        else:
            return False

    def __repr__(self) -> str:
        return ("TreeNode({!r}, {!r}, {!r}, {!r})".format(self.key, self.data, self.left, self.right))


class BinarySearchTree:
    def __init__(self, root_node: Optional[TreeNode] = None):  # Returns empty BST
        self.root: Optional[TreeNode] = root_node

    # returns True if tree is empty, else False
    def is_empty(self) -> bool:
        if self.root is None:
            return True
        else:
            return False

    # returns True if key is in a node of the tree, else False
    def search(self, key: Any) -> bool:
        if self.root is None:
            return False
        else:
            return self.search_helper(self.root, key)

    def search_helper(self, currNode, key) -> Any:
        if key < currNode.key:
            if currNode.left is not None:
                return self.search_helper(currNode.left, key)
        elif key > currNode.key:
            if currNode.right is not None:
                return self.search_helper(currNode.right, key)
        elif key == currNode.key:
            return True
        else:
            return None # pragma: no cover

    # Inserts new node w/ key and data
    # If an item with the given key is already in the BST,
    # the data in the tree will be replaced with the new data
    # Example creation of node: temp = TreeNode(key, data)
    # On insert, can assume key not already in BST
    def insert(self, key: Any, data: Any = None) -> None:
        if self.root is None:
            self.root = TreeNode(key, data)
        else:
            return self.insert_helper(self.root, TreeNode(key, data))

    def insert_helper(self, currNode, newNode) -> Any:
        if newNode.key < currNode.key:
            if currNode.left is None:
                currNode.left = newNode
            else:
                self.insert_helper(currNode.left, newNode)
        elif newNode.key > currNode.key:
            if currNode.right is None:
                currNode.right = newNode
            else:
                self.insert_helper(currNode.right, newNode)

    # returns tuple with min key and associated data in the BST
    # returns None if the tree is empty
    def find_min(self) -> Optional[Tuple[Any, Any]]:
        curr = self.root
        if curr is None:
            return None
        else:
            return self.find_min_helper(curr.left)

    def find_min_helper(self, curr) -> Optional[Tuple[Any, Any]]:
        if curr.left is None:
            return (curr.key, curr.data)
        else:
            return self.find_min_helper(curr.left)

    # returns tuple with max key and associated data in the BST
    # returns None if the tree is empty
    def find_max(self) -> Optional[Tuple[Any, Any]]:
        curr = self.root
        if curr is None:
            return None
        else:
            return self.find_max_helper(curr.right)

    def find_max_helper(self, curr) -> Optional[Tuple[Any, Any]]:
        if curr.right is None:
            return (curr.key, curr.data)
        else:
            return self.find_max_helper(curr.right)

    # returns the height of the tree
    # if tree is empty, return None
    def tree_height(self) -> Optional[int]:
        curr = self.root
        if self.is_empty() is True:
            return None
        else:
            return self.tree_height_helper(curr)

    def tree_height_helper(self, curr) -> Any:
        if curr:
            left = self.tree_height_helper(curr.left)
            right = self.tree_height_helper(curr.right)
            return (max(left, right) + 1)
        else:
            return -1

    # returns Python list of BST keys representing inorder traversal of BST
    def inorder_list(self) -> List:
        if self.root is None:
            return []
        traversal = []
        self.inorder_helper(self.root, traversal)
        return traversal

    def inorder_helper(self, node, trav) -> Any:
        if node:
           self.inorder_helper(node.left, trav)
           trav.append(node.key)
           self.inorder_helper(node.right, trav)

    # returns Python list of BST keys representing preorder traversal of BST
    def preorder_list(self) -> List:
        if self.root is None:
            return []
        traversal = []
        self.preorder_helper(self.root, traversal)
        return traversal

    def preorder_helper(self, node, trav) -> Any:
        if node:
            trav.append(node.key)
            self.preorder_helper(node.left, trav)
            self.preorder_helper(node.right, trav)

    # returns Python list of BST keys representing level-order traversal of BST
    # You MUST use your queue_array data structure from lab 3 to implement this method
    def level_order_list(self) -> List:
        q = Queue(25000)  # Don't change this!
        lista = []
        q.enqueue(self.root)
        if self.root is None:
            return []
        while not q.is_empty():
            curr = q.dequeue()
            if curr.key is not None:
                lista.append(curr.key)
            if curr.left is not None:
                q.enqueue(curr.left)
            if curr.right is not None:
                q.enqueue(curr.right)
        return lista
