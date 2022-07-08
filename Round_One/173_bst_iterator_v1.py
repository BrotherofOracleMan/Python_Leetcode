# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.pointer = -1
        self.inorderList = []
        def inorder(root):
            if root is None:
                return
            inorder(root.left)
            self.inorderList.append(root.val)
            inorder(root.right)
        inorder(root)

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            self.pointer = self.pointer + 1
        return self.inorderList[self.pointer]
            
              

    def hasNext(self):
        """
        :rtype: bool
        """
        return True if self.pointer + 1 < len(self.inorderList) else False
        

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
