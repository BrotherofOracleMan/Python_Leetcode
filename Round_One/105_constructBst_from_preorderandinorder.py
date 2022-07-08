# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.idx = 0
        
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
  
        def buildTreehelper(left,right,inorder_map):
            if left >= right:
                return None
            val = preorder[self.idx]
            
            root = TreeNode(val)
            index = inorder_map[val]
            
            self.idx+=1
            root.left = buildTreehelper(left,index,inorder_map)
            root.right = buildTreehelper(index+1,right,inorder_map)
            
            
            return root
        
        idx_map = {val:idx for idx,val in enumerate(inorder)}
        return buildTreehelper(0,len(preorder),idx_map)
