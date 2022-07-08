# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        parents = {}
        depths = [0,0]

        def fill_dict(child,parent):
            if child is None:
                return 
            parents[child.val] = parent
            fill_dict(child.left,child)
            fill_dict(child.right,child)
    
        fill_dict(root,None)
        
        def getdepth(root,x,y,heights,height,count):
            if root is None:
                return
            if (root.val == x or root.val == y) and count > 0:
                if root.val == y:
                    heights[1] = height
                else:
                    heights[0] = height
                count -=1
                if count == 0:
                    return
            getdepth(root.left,x,y,heights,height+1,2)
            getdepth(root.right,x,y,heights,height+1,2)
            
        
        getdepth(root,x,y,depths,0,2)
        return True if depths[0] == depths[1] and parents[x] != parents[y] else False
           
        
                    
            
            
        
        
        
        
        
        
        
