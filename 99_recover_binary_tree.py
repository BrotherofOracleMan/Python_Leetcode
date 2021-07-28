# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        def recoverTreeHelper(root,trk_list):
            if root is None:
                return
            
            recoverTreeHelper(root.left,trk_list)
            trk_list.append(root.val)
            recoverTreeHelper(root.right,trk_list)
            #tricky part
        def find_two_swapped(nums):
            n = len(nums)
            x = y = -1
            for i in range(n - 1):
                if nums[i + 1] < nums[i]:
                    y = nums[i + 1]
                    if x == -1:
                        x = nums[i]
                    else:           
                        break
            return x, y

        def recover_tree(root,x,y,count):
            if root is None:
                return
            if root.val == x or root.val == y:
                root.val = y if root.val == x else  x
                count -=1
                if count == 0:
                    return
            recover_tree(root.left,x,y,count)
            recover_tree(root.right,x,y,count)
        
        trk_list  = []
        
        if root is not None:
            recoverTreeHelper(root,trk_list)
            x,y = find_two_swapped(trk_list)
            recover_tree(root,x,y,2)
