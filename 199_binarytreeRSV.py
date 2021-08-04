# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def rightSideViewhelper(root,val_list,i):
            if root is None:
                return None
            if len(val_list) == i:
                val_list.append(root.val)
            
            rightSideViewhelper(root.right,val_list,i+1)
            rightSideViewhelper(root.left,val_list,i+1)
        
        
        val_list = []
        rightSideViewhelper(root,val_list,0)
        return val_list
