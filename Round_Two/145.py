# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
            self.post_order_list = []

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def __init__(self):
            self.post_order_list = []

        def postorderHelper(root):
            if root == None:
                return 
            postorderHelper(root.left)
            postorderHelper(root.right)
            self.post_order_list.append(root.val)

        postorderHelper(root)
        return self.post_order_list
