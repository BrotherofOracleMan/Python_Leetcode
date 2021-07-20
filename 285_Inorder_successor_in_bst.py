# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    
    
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        
        inOrderSuccessorOne = None        
        #do a while loop search
        while root != None:
            if root.val > p.val:
                inOrderSuccessorOne = root
                root = root.left
            else:
                root = root.right

        
        return inOrderSuccessorOne 
