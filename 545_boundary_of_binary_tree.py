# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def isLeaf(root):
            return not root.right and not root.left
             
        
        def left_side_helper(root,list_of_tree_nodes):
            while(root != None):
                if not isLeaf(root):
                    list_of_tree_nodes.append(root.val)
                if root.left != None:
                    root = root.left
                else:
                    root = root.right
            return
        
        def right_side_helper(root,list_of_tree_nodes):
            while(root != None):
                if not isLeaf(root):
                    list_of_tree_nodes.append(root.val)
                if root.right != None:
                    root = root.right
                else:
                    root = root.left
            return
        
        def findLeaves(root,list_of_tree_nodes):
            if root is None:
                return
            if isLeaf(root):
                list_of_tree_nodes.append(root.val)
            
            findLeaves(root.left,list_of_tree_nodes)
            findLeaves(root.right,list_of_tree_nodes)
        

        right_side_nodes = []
        final_list = [root.val]
        left_side_helper(root.left,final_list)
        if not isLeaf(root):
            findLeaves(root,final_list)
        right_side_helper(root.right,right_side_nodes)
      
        
        return final_list + right_side_nodes[::-1]
