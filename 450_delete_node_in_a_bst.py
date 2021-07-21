# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getInordersuccessor(self,root):
        if root is None:
            return root.val
        while(root.left != None):
            root = root.left
        return root.val
    
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        #searching component
        if root is None:
            return None
        elif root.val > key:
            root.left = self.deleteNode(root.left,key)
        elif root.val < key:
             root.right = self.deleteNode(root.right,key)
        # delete component
        else:
            if not root.right and not root.left:
                root = None
            elif root.right and not root.left:
                temp = root.right
                del root
                root = temp
            elif root.left and not root.right:
                temp = root.left
                del root
                root = temp
            elif root.left and root.right:
                root.val = self.getInordersuccessor(root.right)
                root.right = self.deleteNode(root.right,root.val)
                return root   
        return root
