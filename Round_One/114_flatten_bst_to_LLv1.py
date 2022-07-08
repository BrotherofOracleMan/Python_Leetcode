# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        def preorder(root,val_list):
            if root is None:
                return 
            val_list.append(root.val)
            preorder(root.left,val_list)
            preorder(root.right,val_list)
        
        if root is None:
            return
        
        val_list = []
        preorder(root,val_list)
        print(val_list)
        
        for i in range(len(val_list)):
            if i == 0:
                root.val = val_list[0]
                root.left = None
                root.right = None
            else:
                root.right = TreeNode(val_list[i])
                root = root.right
