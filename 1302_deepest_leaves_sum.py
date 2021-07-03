# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        node_list = []
        node_stack = []
        deepest_value = 0
        deepest_sum =0
        node_stack.append([root,0])
        
        if root is None:
            return 0
        
        
        while len(node_stack) != 0:
            
            current_node = node_stack[-1][0]
            current_depth = node_stack[-1][1]
            node_stack.pop()
            
            node_list.append([current_node.val,current_depth])
            deepest_value = max(deepest_value,current_depth)
            if current_node.left:
                node_stack.append([current_node.left,current_depth+1])
            if current_node.right:
                node_stack.append([current_node.right,current_depth+1])
            
        for pair in node_list:
            if pair[1] == deepest_value:
                deepest_sum += pair[0]    
        return deepest_sum