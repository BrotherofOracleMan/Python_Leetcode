# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.preorder_list = []

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def preorderHelper(root):
            if root == None:
                return 
            self.preorder_list.append(root.val)
            preorderHelper(root.left)
            preorderHelper(root.right)
        preorderHelper(root)
        return self.preorder_list
