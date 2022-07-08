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
        self.stack = []
        
        self.left_most_inorder(root,self.stack)
        
    def left_most_inorder(self,root,stack):
        
        while root:
            self.stack.append(root)
            root = root.left
        
        
    def next(self):
        """
        :rtype: int
        """
        topmost_node = self.stack.pop()
        
        if topmost_node.right:
            self.left_most_inorder(topmost_node.right,self.stack)
        
        return topmost_node.val        

    def hasNext(self):
        """
        :rtype: bool
        """
        return True if len(self.stack) > 0 else False
        

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
