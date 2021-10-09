# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        range_list = []
        
        def iterate_and_check(low, high, range_list, root):
            if root is None:
                return
            if low <=root.val <= high:
                range_list.append(root.val)
            
            iterate_and_check(low,high,range_list,root.left)
            iterate_and_check(low,high,range_list,root.right)
        
        val_list = []
        iterate_and_check(low,high,val_list,root)
        
        return sum(val_list)