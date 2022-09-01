# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        def find_left_most(node, left_list):
            if not node or (not node.left and not node.right):
                return
            elif node.left:
                left_list.append(node.val)
                find_left_most(node.left,left_list)
            elif node.right:
                left_list.append(node.val)
                find_left_most(node.right,left_list)
        
        def find_leave_nodes(node,leaf_list):
            stack = [root]
            while len(stack) > 0:
                pop_node = stack.pop()
                if pop_node:
                    if not pop_node.left and not pop_node.right and pop_node != root:
                        leaf_list.append(pop_node.val)
                    stack.append(pop_node.left)
                    stack.append(pop_node.right)
        def find_right_most(node, right_list):
            if not node or (not node.left and not node.right):
                return
            elif node.right:
                right_list.append(node.val)
                find_right_most(node.right,right_list)
            elif node.left:
                right_list.append(node.val)
                find_right_most(node.left,right_list)
        root_list = [root.val] 
        left_most =[]
        leaf_nodes = []
        right_most = []
        find_left_most(root.left,left_most)
        find_leave_nodes(root,leaf_nodes)
        find_right_most(root.right,right_most)
        return root_list + left_most + leaf_nodes[::-1] + right_most[::-1]
        
