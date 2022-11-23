"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution(object):
    def __init__(self):
        self.previous = None
        self.inorderSuccessorNode = None
        self.root = None

    def inorderSuccessor(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            self.inorderSuccessorNode = node
        else:
            self.root = node
            while self.root.parent:
                self.root = self.root.parent
            self.inorderHelper(self.root,node)
        return self.inorderSuccessorNode

    def inorderHelper(self,root,p):
        if root:
            self.inorderHelper(root.left,p)
            if self.previous == p and not self.inorderSuccessorNode:
                self.inorderSuccessorNode = root
            self.previous = root
            self.inorderHelper(root.right,p)
        return self.inorderSuccessorNode
